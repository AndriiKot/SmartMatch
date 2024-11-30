import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Find similar songs based on input text.')
    parser.add_argument('--data_folder', type=str, default='data/', help='Folder containing song text files.')
    parser.add_argument('--files_source', type=str, default='*.txt', help='File pattern to search for song files.')
    parser.add_argument('--max_words', type=int, default=200, help='Maximum number of words to consider in the text.')
    return parser.parse_args()

