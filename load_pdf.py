import fitz  # PyMuPDF for PDF processing

def extract_pdf_text(file_path):
    """Extract text from a PDF file at the specified path."""
    with fitz.open(file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text
