from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils.parse_arguments import parse_arguments
from utils import load_texts


def get_vector(model, tokenizer, text, max_words):
    words = text.split()
    limited_words = words[:max_words]
    limited_text = ' '.join(limited_words)
    inputs = tokenizer(limited_text, return_tensors='pt', truncation=True, padding='max_length')

    with torch.no_grad():
        outputs = model(**inputs)

    return outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()

def find_similar_text(user_input, vectors, text_names, model, tokenizer, max_words):
    user_vector = get_vector(model, tokenizer, user_input, max_words)
    similarities = cosine_similarity([user_vector], vectors)
    most_similar_index = np.argmax(similarities)
    most_similar_text = text_names[most_similar_index]
    similarity_score = similarities[0][most_similar_index]
    return most_similar_text, similarity_score

# Main code execution
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
similar_text_name, similarity_score = find_similar_text(user_input, vectors, text_names, model, tokenizer, args.max_words)
print(f"The most similar document is: {similar_text_name} with a similarity score of {similarity_score:.4f}")
