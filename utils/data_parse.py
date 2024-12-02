import os

class Song:
    def __init__(self, filename):
        self.filename = filename
        self.title = self.extract_title()
        self.content = self.extract_content()

    def extract_title(self):
        print(f"Extracting title for {self.filename}...")

    def extract_content(self):
        print(f"Extracting content for {self.filename}...")


song = Song("song.txt")

print(song)
print(song.title)
print(song.content)
