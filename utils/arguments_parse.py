import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Find similar songs based on input text.')
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument('--data_folder', type=str, default='data/', help='Folder containing song text files.')
        self.parser.add_argument('--files_source', type=str, default='*.txt', help='File pattern to search for song files.')
        self.parser.add_argument('--max_words', type=int, default=200, help='Maximum number of words to consider in the text.')

    def parse_arguments(self):
        return self.parser.parse_args()
