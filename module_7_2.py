import io

from pprint import pprint

file_name = 'text.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings, 1):
        strings_positions[i, file.tell()] = string
        file.write(string + '\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('text.txt', info)
for elem in result.items():
  print(elem)
