from transformers import Trainer, TrainingArguments

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',  
    num_train_epochs=3,  
    per_device_train_batch_size=2,  
    per_device_eval_batch_size=2,
    logging_dir='./logs',
    logging_steps=10,
)

# Trainer setup
trainer = Trainer(
    model=model,  
    args=training_args,  
    train_dataset=dataset,
)

# Start training (this part could take time based on your dataset size)
trainer.train()
