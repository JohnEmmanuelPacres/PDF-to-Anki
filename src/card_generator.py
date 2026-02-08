import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- FIX 1: ADD num_cards=10 HERE ---
def generate_flashcards(text_content, num_cards=10):
    """
    Sends text to Gemini and returns a list of flashcards.
    """
    try:
        model = genai.GenerativeModel('gemini-3-flash-preview')
    except:
        model = genai.GenerativeModel('gemini-3-pro-preview')

    # The Prompt
    prompt = f"""
    You are an expert tutor. Create exactly {num_cards} Anki flashcards based on the text below.
    Focus on the most important concepts, definitions, and relationships.
    
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
        response = model.generate_content(prompt)
        
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