from transformers import BartTokenizer, BartForConditionalGeneration

# Load tokenizer and model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Tokenize a sample text for testing
inputs = tokenizer(dataset['text'][0], max_length=1024, return_tensors='pt', truncation=True)

# Generate summary
summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Generated Summary:", summary)
