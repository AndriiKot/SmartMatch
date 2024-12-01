from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_texts, get_vector, parse_arguments

class Vectorizer:
    def __init__(self, model_name, max_words):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.max_words = max_words

    def get_vector(self, text):
        return get_vector(self.model, self.tokenizer, text, self.max_words)

class SimilarityCalculator:
    def __init__(self, vectors, text_names):
        self.vectors = vectors
        self.text_names = text_names

    def find_similar_text(self, user_vector):
        similarities = cosine_similarity([user_vector], self.vectors)
        most_similar_index = np.argmax(similarities)
        most_similar_text = self.text_names[most_similar_index]
        similarity_score = similarities[0][most_similar_index]
        return most_similar_text, similarity_score

class TextSimilarityFinder:
    def __init__(self, model_name, data_folder, files_source, max_words):
        self.texts = load_texts(data_folder, files_source)
        self.vectorizer = Vectorizer(model_name, max_words)
        self.vectors = np.array([self.vectorizer.get_vector(text) for text in self.texts.values()])
        self.text_names = list(self.texts.keys())
        self.similarity_calculator = SimilarityCalculator(self.vectors, self.text_names)


    def get_user_input_vector(self):
        user_input = input("Please enter the text you want to find a similar document for: ")

        if not user_input.strip():
            print("Input cannot be empty. Please enter valid text.")
            return None

        return self.vectorizer.get_vector(user_input)

    def run(self):
        user_vector = self.get_user_input_vector()
        similar_text_name, similarity_score = self.similarity_calculator.find_similar_text(user_vector)
        print(f"The most similar document is: {similar_text_name} with a similarity score of {similarity_score:.4f}")

if __name__ == "__main__":
    similarity_finder = TextSimilarityFinder(
        model_name="distilbert-base-uncased",
        **{key: vars(parse_arguments())[key] for key in ['data_folder', 'files_source', 'max_words']}
    )
    similarity_finder.run()

