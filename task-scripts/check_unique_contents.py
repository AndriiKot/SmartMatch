import os

def normalize_content(content):
    return ''.join(content.split()).lower()

def check_unique_contents(directory):
    content_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                normalized_content = normalize_content(content)

                if normalized_content in content_dict:
                    print(f'The content of the file "{filename}" is not unique. It duplicates the content from the file "{content_dict[normalized_content]}".')
                else:
                    content_dict[normalized_content] = filename

    if len(content_dict) == len(os.listdir(directory)):
        print("Check complete, all files are unique.")

check_unique_contents('../data/')
