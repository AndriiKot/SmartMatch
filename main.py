import os
import glob
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

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
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=MAX_WORDS, padding='max_length')
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

song_names = list(songs.keys())

first_song_name = song_names[0]
first_song_text = songs[first_song_name]

print(f"Название первой песни: {first_song_name}")
print(f"Текст первой песни: {first_song_text}")

# Получаем вектор первой песни
first_song_vector = get_vector(first_song_text)
print(first_song_vector)

