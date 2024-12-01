from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_texts, get_vector, parse_arguments

class TextSimilarityFinder:
    def __init__(self, model_name, data_folder, files_source, max_words):
        print("Initializing TextSimilarityFinder...", self)
        print("Model name:", model_name)
        print("Data folder:", data_folder)
        print("Files source:", files_source)
        print("Max words:", max_words)

if __name__ == "__main__":
    similarity_finder = TextSimilarityFinder(
        model_name="distilbert-base-uncased",
        **{key: vars(parse_arguments())[key] for key in ['data_folder', 'files_source', 'max_words']}
    )
