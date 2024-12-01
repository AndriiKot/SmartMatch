import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel

class Vectorizer:
    def __init__(self, model_name, max_words):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.max_words = max_words

    def get_vector(self, text):
        words = text.split()
        limited_words = words[:self.max_words]
        limited_text = ' '.join(limited_words)
        inputs = self.tokenizer(limited_text, return_tensors='pt', truncation=True, padding='max_length').to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)

        return outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
