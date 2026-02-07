import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_flashcards(text_content):
    """
    Sends text to Gemini and returns a list of flashcards.
    
    Args:
        text_content (str): The text from the PDF.
        
    Returns:
        list: A list of dicts [{'front': '...', 'back': '...'}]
    """
    
    # Initialize the model
    # "gemini-1.5-flash" is great for this. Use "gemini-1.5-pro" for complex topics.
    model = genai.GenerativeModel('gemini-1.5-flash')

    # The Prompt
    # We ask for a specific JSON schema so we can parse it easily.
    prompt = f"""
    You are an expert tutor. Create 10 anki flashcards based on the text below.
    
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
        # Generate content
        response = model.generate_content(prompt)
        
        # Clean the response text (sometimes models add markdown backticks)
        clean_text = response.text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
            
        # Parse JSON
        flashcards = json.loads(clean_text)
        return flashcards

    except Exception as e:
        print(f"Error generating flashcards: {e}")
        # Return an empty list or a dummy card so the app doesn't crash
        return []