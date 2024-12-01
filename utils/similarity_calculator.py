import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityCalculator:
    def __init__(self, vectors, text_names):
        self.vectors = np.array(vectors)  # Преобразуем список в массив numpy
        self.text_names = text_names

    def find_similar_text(self, user_vector):
        similarities = cosine_similarity([user_vector], self.vectors)
        most_similar_index = np.argmax(similarities)
        most_similar_text = self.text_names[most_similar_index]
        similarity_score = similarities[0][most_similar_index]
        return most_similar_text, similarity_score
