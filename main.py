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

print(AutoModel, AutoTokenizer)
