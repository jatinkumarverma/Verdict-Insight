from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Simple preprocessing function
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Join tokens back into a cleaned string
    return " ".join(tokens)

preprocessed_texts = [preprocess_text(text) for text in extracted_texts]
