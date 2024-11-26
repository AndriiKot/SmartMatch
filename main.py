import os
import glob

data_folder = 'data/'

songs = {}
for filepath in glob.glob(os.path.join(data_folder, '*.txt')):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        song_name = os.path.basename(filepath)
        songs[song_name] = text

processed_songs = {}
for song_name, text in songs.items():
    print(f"Обработка песни: {song_name}")
    print(f"Текст песни: {text}")
