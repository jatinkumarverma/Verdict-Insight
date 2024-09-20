import fitz  # PyMuPDF
import os

# Assuming PDFs are in a folder named 'pdfs/'
pdf_folder = 'pdfs/'
extracted_texts = []

for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        doc = fitz.open(os.path.join(pdf_folder, pdf_file))
        text = ""
        for page in doc:
            text += page.get_text()
        extracted_texts.append(text)

# Now 'extracted_texts' is a list of strings, where each string is the content of one PDF.
