import os
import glob

data_folder = 'data/'
files_source = "*.txt"
max_words = 2

songs = {}
for filepath in glob.glob(os.path.join(data_folder, files_source)):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        song_name = os.path.basename(filepath)
        songs[song_name] = text

processed_songs = {}
for song_name, text in songs.items():
    processed_text = ' '.join(text.split()[:max_words])
    processed_songs[song_name] = processed_text

print(processed_songs)
