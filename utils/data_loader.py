import glob
import os

class DataLoader:
    def __init__(self, data_folder, files_source):
        self.data_folder = data_folder
        self.files_source = files_source
        self.texts = {}

    def load_texts(self):
        for filepath in glob.glob(os.path.join(self.data_folder, self.files_source)):
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
                text_name = os.path.basename(filepath)
                self.texts[text_name] = text
        return self.texts
