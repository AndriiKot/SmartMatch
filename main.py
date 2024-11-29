from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_texts, get_vector, parse_arguments


def find_similar_text(user_vector, vectors, text_names):
    similarities = cosine_similarity([user_vector], vectors)
    most_similar_index = np.argmax(similarities)
    most_similar_text = text_names[most_similar_index]
    similarity_score = similarities[0][most_similar_index]
    return most_similar_text, similarity_score

args = parse_arguments()
texts = load_texts(args.data_folder, args.files_source)

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

vectors = np.array([get_vector(model, tokenizer, text, args.max_words) for text in texts.values()])
text_names = list(texts.keys())

user_input = input("Please enter the text you want to find a similar document for: ")
user_vector = get_vector(model, tokenizer, user_input, args.max_words)
similar_text_name, similarity_score = find_similar_text(user_vector, vectors, text_names)
print(f"The most similar document is: {similar_text_name} with a similarity score of {similarity_score:.4f}")
