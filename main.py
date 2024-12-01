from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_texts, get_vector, parse_arguments

class TextSimilarityFinder:
    def __init__(self, model_name, data_folder, files_source, max_words):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.max_words = max_words
        self.texts = load_texts(data_folder, files_source)
        self.text_names = list(self.texts.keys())
        # self.vectors = np.array([self.get_vector(text) for text in self.texts.values()])

    def get_vector(self, text):
        return get_vector(self.model, self.tokenizer, text, self.max_words)

    def get_user_input_vector(self):
        user_input = input("Please enter the text you want to find a similar document for: ")
        # return self.get_vector(user_input)



if __name__ == "__main__":
    similarity_finder = TextSimilarityFinder(
        model_name="distilbert-base-uncased",
        **{key: vars(parse_arguments())[key] for key in ['data_folder', 'files_source', 'max_words']}
    ).get_user_input_vector()
