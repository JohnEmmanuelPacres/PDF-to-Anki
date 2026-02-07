# PDF to Anki Generator

A streamlined Python application that converts PDF documents (textbooks, lecture slides, notes) into ready-to-use Anki flashcard decks (`.apkg`) using Google's Gemini AI.

### Features

- **PDF Text Extraction:** Upload any PDF file and automatically extract the text content.
- **AI-Powered Generation:** Uses Google's **Gemini 1.5 Flash** model to intelligently generate high-quality question-and-answer pairs.
- **Customizable Output:** Choose exactly how many flashcards you want to generate (from 5 to 50).
- **Direct Export:** Generates a `.apkg` file that can be directly imported into the Anki desktop or mobile app.
- **Clean UI:** Built with **Streamlit** for a simple, responsive user interface.

## Tech Stack

- **Frontend:** Streamlit
- **AI Model:** Google Gemini (via `google-generativeai`)
- **PDF Processing:** PyMuPDF (`fitz`)
- **Anki Generation:** `genanki`
- **Language:** Python 3.10+

## Project Structure

```text
PDF-to-Anki/
│
├── .env                    # API keys (Not tracked by Git)
├── .gitignore              # Files to ignore
├── requirements.txt        # Dependencies
├── main.py                 # The entry point (Streamlit UI)
├── README.md               # Documentation
│
└── src/                    # Source code
    ├── __init__.py
    ├── pdf_loader.py       # Handles PDF text extraction
    ├── card_generator.py   # Interactions with Gemini API
    └── anki_builder.py     # Generates the .apkg file
```
