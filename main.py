import os
import glob
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

data_folder = 'data/'
files_source = "*.txt"
MAX_WORDS = 200

songs = {}
for filepath in glob.glob(os.path.join(data_folder, files_source)):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        song_name = os.path.basename(filepath)
        songs[song_name] = text

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_vector(text):
    words = text.split()
    limited_words = words[:MAX_WORDS]
    limited_text = ' '.join(limited_words)
    inputs = tokenizer(limited_text, return_tensors='pt', truncation=True, padding='max_length')
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

vectors = []

song_names = list(songs.keys())

for song_name in song_names:
    song_vector = get_vector(songs[song_name])
    vectors.append(song_vector)

vectors = np.array(vectors)

print(cosine_similarity)
