import os
import streamlit as st
from src import extract_text, generate_flashcards, build_deck
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="PDF to Anki", page_icon="📚")

st.title("PDF to Anki 📚")

with st.sidebar: # Sidebar for settings
    st.header("Settings")
    # API key handling
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.warning("GEMINI_API_KEY not found in environment variables. Please set it in your .env file.")
        st.text_input("Enter API key", type = 'password', key = 'user_api_key')
    
    # Slider for how many cards to generate
    num_cards = st.slider('Number of flashcards to generate', min_value=5, max_value=50, value=10, step = 5)
    deck_name = st.text_input("Deck name", value="My Flashcards")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner('Extracting text from PDF...'):
        text = extract_text(uploaded_file)
    
    st.success(f"Loaded{len(text)} characters from PDF.")

    if st.button('Generate Flashcards'):
        with st.spinner(f'Generating {num_cards} flashcards...'):
            cards = generate_flashcards(text, num_cards)

            if cards:
                st.write('### Preview')
                st.json(cards[:3]) # Show first 3 cards as preview

                # Build the Anki deck
                deck_path = build_deck(cards, deck_name)

                with open(deck_path, 'rb') as f:
                    st.download_button(
                        label='Download Anki Deck (.apkg)',
                        data = f,
                        file_name = deck_path,
                        mime = 'application/octet-stream'
                    )
            else:
                st.error("Failed to generate flashcards. Please try again.")


