import streamlit as st
from src import extract_text, generate_flashcards, build_deck
from dotenv import load_dotenv

load_dotenv()

st.title("PDF to Anki")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    text = extract_text(uploaded_file)

    if st.button("Generate Cards"):
        cards = generate_flashcards(text)

        deck_path = build_deck(cards, "My Deck")
        with open(deck_path, "rb") as f:
            st.download_button("Download Anki Deck", f, file_name="my_deck.apkg")


