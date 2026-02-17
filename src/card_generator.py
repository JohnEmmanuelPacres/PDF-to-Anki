from google import genai
from google.genai import types
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_flashcards(text_content, num_cards=10):
    """
    Sends text to Gemini and returns a list of flashcards.
    """
    try:
        model = 'gemini-3-flash-preview'
    except:
        model = 'gemini-3-pro-preview'

    # The Prompt
    prompt = f"""
    You are an expert tutor. Create exactly {num_cards} Anki flashcards based on the text below.
    Focus on the most important concepts, definitions, and relationships. As much as possible focus on creating question-answer pairs that test understanding, 
    not just recall. Use simple language and be concise. Also add true or false questions if applicable.
    
    Strictly follow this JSON format:
    [
      {{ "front": "Question here", "back": "Answer here" }},
      {{ "front": "Question here", "back": "Answer here" }}
    ]
    
    Do not add markdown formatting like ```json ... ```. Just return the raw JSON array.
    
    TEXT TO PROCESS:
    {text_content}
    """
    
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0,
                top_p=0.95,
                top_k=20,
            ),
        )
        
        # Clean the response text
        clean_text = response.text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
            
        flashcards = json.loads(clean_text)
        return flashcards

    except Exception as e:
        print(f"Error generating flashcards: {e}")
        return []