import torch
from transformers import BartTokenizer, BartForConditionalGeneration
import argparse

# Load the model and tokenizer
def load_model(model_path):
    print("Loading model from", model_path)
    model = BartForConditionalGeneration.from_pretrained(model_path)
    tokenizer = BartTokenizer.from_pretrained(model_path)
    model.eval()  # Set model to evaluation mode
    return model, tokenizer

# Function to generate summaries
def generate_summary(model, tokenizer, input_text, max_length=150, num_beams=4):
    # Tokenize input text
    inputs = tokenizer(input_text, return_tensors='pt', truncation=True, padding=True)
    
    # Generate summary
    summary_ids = model.generate(
        inputs['input_ids'], 
        num_beams=num_beams, 
        max_length=max_length, 
        early_stopping=True
    )
    
    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run inference for Legal Summarization")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the trained model")
    parser.add_argument("--input_text", type=str, required=True, help="Text of the legal judgment to summarize")
    parser.add_argument("--output_path", type=str, default="summary.txt", help="File to save the generated summary")
    
    args = parser.parse_args()
    
    # Load the trained model and tokenizer
    model, tokenizer = load_model(args.model_path)
    
    # Read the input text (legal judgment) from a file
    with open(args.input_text, "r", encoding="utf-8") as f:
        legal_text = f.read()
    
    # Generate the summary
    print("Generating summary...")
    summary = generate_summary(model, tokenizer, legal_text)
    
    # Save the summary to the output file
    with open(args.output_path, "w", encoding="utf-8") as f:
        f.write(summary)
    
    print(f"Summary generated and saved to {args.output_path}")
