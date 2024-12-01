from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_texts, get_vector, parse_arguments

class TextSimilarityFinder:
    def __init__(self, model_name, data_folder, files_source, max_words):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        print("Loading texts...", self)
        print("Tokens:", self.tokenizer)
        print("Model:", self.model)


if __name__ == "__main__":
    similarity_finder = TextSimilarityFinder(
        model_name="distilbert-base-uncased",
        **{key: vars(parse_arguments())[key] for key in ['data_folder', 'files_source', 'max_words']}
    )
