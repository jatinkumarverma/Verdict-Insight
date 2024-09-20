from torch.optim import Adam
import torch

# Set the model to training mode
model.train()

# Placeholder for model fine-tuning with RL
optimizer = Adam(model.parameters(), lr=1e-5)

# Define the number of epochs
epochs = 3  # Example value, adjust as needed

# Iterate over epochs
for epoch in range(epochs):
    for idx, text in enumerate(dataset['text']):
        # Tokenize input
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=1024) # Added max_length

        # Ensure inputs are on the correct device (e.g., GPU if available)
        inputs = {key: val.to(model.device) for key, val in inputs.items()}

        # Generate summary
        summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)
        generated_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Compute reward (assuming custom_reward returns a tensor)
        reward = custom_reward(generated_summary, text)
        
        # Convert reward to tensor and set requires_grad to True
        reward = torch.tensor(reward, device=model.device, requires_grad=True)

        # Compute loss (negative reward, we aim to minimize the negative reward)
        loss = -reward
        loss.backward()

        # Optimizer step
        optimizer.step()
        optimizer.zero_grad()

        # Detach the loss for logging
        print(f"Epoch: {epoch}, Batch: {idx}, Loss: {loss.item()}")