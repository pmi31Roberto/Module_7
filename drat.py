file = open('example.txt', 'a', encoding='UTF-8')
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
for i in info:
    file.write(f'{i}\n')