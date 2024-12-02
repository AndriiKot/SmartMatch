import os

class Song:
    def __init__(self, data_folder, files_source):
        self.data_folder = data_folder
        self.files_source = files_source
        self.file_path = os.path.join(self.data_folder, self.files_source)
        self.title = self.extract_title()
        self.content = self.extract_content()

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.readlines()

    def extract_title(self):
        lines = self.read_file()
        first_line = lines[0].strip()
        if first_line.startswith('Title:'):
            return first_line.split('"')[1]
        elif first_line.startswith('"') and first_line.endswith('"'):
            return first_line.strip('"')
        else:
            return "Unknown Title"
    def extract_content(self):
        lines = self.read_file()
        return ''.join(lines)

