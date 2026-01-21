import json
import re
from typing import List, Dict

def clean_text(text: str) -> str:
    """
    Clean and preprocess text data.
    """
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text.strip())
    # Remove special characters (keep basic punctuation)
    text = re.sub(r'[^\w\s.,!?]', '', text)
    return text.lower()

def preprocess_dialogues(input_file: str, output_file: str) -> None:
    """
    Preprocess raw dialogue data and save to processed format.
    """
    processed_data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            dialogue = json.loads(line.strip())
            # Assuming dialogue has 'input' and 'output' fields
            cleaned_input = clean_text(dialogue.get('input', ''))
            cleaned_output = clean_text(dialogue.get('output', ''))
            processed_data.append({
                'input': cleaned_input,
                'output': cleaned_output
            })

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in processed_data:
            f.write(json.dumps(item) + '\n')

    print(f"Processed {len(processed_data)} dialogues")

if __name__ == "__main__":
    preprocess_dialogues('../data/raw/dialogues.jsonl', '../data/processed/train.jsonl')
