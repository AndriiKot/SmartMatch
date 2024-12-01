import numpy as np
import faiss

class SimilarityCalculator:
    def __init__(self, vectors, text_names):
        self.vectors = np.array(vectors).astype('float32')
        self.text_names = text_names

        self.index = faiss.IndexFlatL2(self.vectors.shape[1])
        self.index.add(self.vectors)  

    def find_similar_text(self, user_vector):
        user_vector = np.array(user_vector).astype('float32').reshape(1, -1)  # Преобразуем вектор пользователя в нужный формат
        distances, indices = self.index.search(user_vector, 1)  # Ищем 1 ближайший сосед

        most_similar_index = indices[0][0]
        most_similar_text = self.text_names[most_similar_index]
        similarity_score = 1 / (1 + distances[0][0])  # Преобразуем расстояние в коэффициент схожести (0-1)

        return most_similar_text, similarity_score
