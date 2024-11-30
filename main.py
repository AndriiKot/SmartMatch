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
    args = parse_arguments()
    similarity_finder = TextSimilarityFinder(
        model_name="distilbert-base-uncased",
        data_folder=args.data_folder,
        files_source=args.files_source,
        max_words=args.max_words
    )
