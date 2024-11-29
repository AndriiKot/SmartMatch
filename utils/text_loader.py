import glob
import os

def load_texts(data_folder, files_source):
    texts = {}
    for filepath in glob.glob(os.path.join(data_folder, files_source)):
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            text_name = os.path.basename(filepath)
            texts[text_name] = text
    return texts

