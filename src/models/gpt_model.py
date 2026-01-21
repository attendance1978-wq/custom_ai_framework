from transformers import GPT2LMHeadModel

def load_gpt_model(path):
    """
    Load GPT model from the given path.
    """
    return GPT2LMHeadModel.from_pretrained(path)
