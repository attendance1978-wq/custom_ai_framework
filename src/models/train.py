import torch
from transformers import Trainer, TrainingArguments
from src.data.dataset import ChatbotDataset
from src.models.gpt_model import load_gpt_model
from transformers import GPT2Tokenizer

def train_model(tokenizer_path='../models/tokenizer', 
                model_path='../models/base', 
                data_path='../data/processed/train.jsonl', 
                output_dir='../models/fine_tuned',
                num_epochs=3, batch_size=4):
    """
    Train the GPT model on the chatbot dataset.
    """
    # Load tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    model = load_gpt_model(model_path)
    
    # Load dataset
    train_dataset = ChatbotDataset(data_path, tokenizer)
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=num_epochs,
        per_device_train_batch_size=batch_size,
        save_steps=500,
        save_total_limit=2,
        logging_dir='../logs',
    )
    
    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )
    
    # Train
    trainer.train()
    trainer.save_model(output_dir + '/checkpoint-1000')
    
    print("Training completed")
