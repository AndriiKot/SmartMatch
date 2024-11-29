import os
import glob
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils.parse_arguments import parse_arguments  # Импортируем нужную функцию

args = parse_arguments()

songs = {}

for filepath in glob.glob(os.path.join(args.data_folder, args.files_source)):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        song_name = os.path.basename(filepath)
        songs[song_name] = text

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def get_vector(text):
    words = text.split()
    limited_words = words[:args.max_words]
    limited_text = ' '.join(limited_words)
    inputs = tokenizer(limited_text, return_tensors='pt', truncation=True, padding='max_length')

    with torch.no_grad():
        outputs = model(**inputs)

    return outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()

vectors = []
song_names = list(songs.keys())

for song_name in song_names:
    song_vector = get_vector(songs[song_name])
    vectors.append(song_vector)

vectors = np.array(vectors)

def find_similar_song(user_input):
    user_vector = get_vector(user_input)
    similarities = cosine_similarity([user_vector], vectors)
    most_similar_index = np.argmax(similarities)
    most_similar_song = song_names[most_similar_index]
    similarity_score = similarities[0][most_similar_index]
    return most_similar_song, similarity_score

user_input = input("Please enter the text you want to find a similar song for: ")
similar_song_name, similarity_score = find_similar_song(user_input)
print(f"The most similar song is: {similar_song_name} with a similarity score of {similarity_score:.4f}")
