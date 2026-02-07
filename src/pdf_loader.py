import fitz

def extract_text(uploaded_file):
    # Open the PDF file
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()
    
    return text