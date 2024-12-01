from utils import Vectorizer, SimilarityCalculator, DataLoader, ArgumentParser

class TextSimilarityFinder:
    def __init__(self, model_name, data_folder, files_source, max_words):
        self.data_loader = DataLoader(data_folder, files_source)
        self.texts = self.data_loader.load_texts()
        self.vectorizer = Vectorizer(model_name, max_words)
        self.vectors = [self.vectorizer.get_vector(text) for text in self.texts.values()]
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
        if user_vector is None:
            return
        similar_text_name, similarity_score = self.similarity_calculator.find_similar_text(user_vector)
        print(f"The most similar document is: {similar_text_name} with a similarity score of {similarity_score:.4f}")

if __name__ == "__main__":
    similarity_finder = TextSimilarityFinder(
        model_name="distilbert-base-uncased",
        **{key: vars(ArgumentParser().parse_arguments())[key] for key in ['data_folder', 'files_source', 'max_words']}
    )
    similarity_finder.run()
