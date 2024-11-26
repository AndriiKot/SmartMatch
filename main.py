import os
import glob

data_folder = 'data/'

songs = {}
for filepath in glob.glob(os.path.join(data_folder, '*.txt')):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        song_name = os.path.basename(filepath)
        songs[song_name] = text

print("\n\nFile reading completed. Found songs:", list(songs.keys()), "\n\n")
print(songs)
