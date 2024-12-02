import os

class Song:
    def __init__(self, data_folder, files_source):
        self.data_folder = data_folder
        self.files_source = files_source
        self.file_path = os.path.join(self.data_folder, self.files_source)
        self.title, self.content = self.extract_info()

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.readlines()

    def extract_info(self):
        lines = self.read_file()
        first_line = lines[0].strip()
        title = self.extract_title(first_line)
        content = ''.join(lines)

        return title, content

    def extract_title(self, first_line):
        if first_line.startswith('Title:'):
            return first_line.split('"')[1] if '"' in first_line else "Unknown Title"
        elif first_line.startswith('"') and first_line.endswith('"'):
            return first_line.strip('"')
        else:
            return "Unknown Title"

