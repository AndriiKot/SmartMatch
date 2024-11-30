from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_texts, get_vector, parse_arguments

class TextSimilarityFinder:
    def __init__(self):
        print("Initializing TextSimilarityFinder...", self)


similarity_finder = TextSimilarityFinder()
