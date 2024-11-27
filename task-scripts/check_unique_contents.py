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
                    print(f'Содержимое файла "{filename}" не уникально. Повторяется с файлом "{content_dict[normalized_content]}".')
                else:
                    content_dict[normalized_content] = filename

    print("Проверка завершена.")

check_unique_contents('../data/')

