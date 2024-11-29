import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel

def get_vector(model, tokenizer, text, max_words):
    words = text.split()
    limited_words = words[:max_words]
    limited_text = ' '.join(limited_words)
    inputs = tokenizer(limited_text, return_tensors='pt', truncation=True, padding='max_length')

    with torch.no_grad():
        outputs = model(**inputs)

    return outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
