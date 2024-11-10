def custom_write(file_name, strings):
    strings_positions = {}
    bait = []
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')
        bait.append(file.tell)

    file.close()

    file = open(file_name, 'r', encoding='utf-8')
    content = file.readlines()
    cou = 1
    file.seek(0)
    for string in content:
        position = file.tell()
        strings_positions[(cou, position)] = string.strip()
        cou += 1
        file.readline()
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
