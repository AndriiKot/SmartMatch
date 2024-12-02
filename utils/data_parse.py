import os

class Song:
    def __init__(self, data_folder, files_source):
        self.data_folder = data_folder
        self.files_source = files_source
        self.title = self.extract_title()
        self.content = self.extract_content()

    def extract_title(self):
        with open(os.path.join(self.data_folder, self.files_source), 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line.startswith('Title:'):
                return first_line.split('"')[1]
            elif first_line.startswith('"') and first_line.endswith('"'):
                return first_line.strip('"')
            else:
                return "Unknown Title"

    def extract_content(self):
        print(f"Extracting content for {self.files_source}...")


