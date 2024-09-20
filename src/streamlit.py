import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
import fitz  # PyMuPDF for PDF handling
import os

# Load the tokenizer and model (you can change this to your fine-tuned model path)
@st.cache(allow_output_mutation=True)
def load_model():
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    return tokenizer, model

tokenizer, model = load_model()

# Title of the app
st.title("Legal Judgment Summarizer")

# File uploader (for PDF or text file)
uploaded_file = st.file_uploader("Upload a legal judgment (PDF or text)", type=["pdf", "txt"])

# Function to extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Text summarization function
def generate_summary(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=1024)
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=150, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
    
    # Display extracted text
    st.subheader("Extracted Text")
    st.write(text[:2000] + "...")  # Display the first 2000 characters for brevity
    
    # Button to summarize the text
    if st.button("Generate Summary"):
        summary = generate_summary(text)
        st.subheader("Generated Summary")
        st.write(summary)
