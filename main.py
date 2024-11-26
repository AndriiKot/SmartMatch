import os
import glob
from transformers import AutoTokenizer, AutoModel

data_folder = 'data/'
files_source = "*.txt"

songs = {}
for filepath in glob.glob(os.path.join(data_folder, files_source)):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        song_name = os.path.basename(filepath)
        songs[song_name] = text

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

print("Model name:", model_name)
print("Number of songs:", len(songs))
print("Number of tokens:", sum(len(tokenizer.encode(song)) for song in songs.values()))
