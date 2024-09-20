from datasets import Dataset

# Create a dataset from the list of texts
dataset = Dataset.from_dict({"text": preprocessed_texts})

# Example of viewing the dataset
print(dataset)