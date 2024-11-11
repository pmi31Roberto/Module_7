def remove_punctuation(line):
    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
    for punct in punctuation:
        for char in line:
            if char == punct:
                line = line.replace(char, '')
    return line


a = 'Its! a. text for task= Найти везде,'
line = remove_punctuation(a.lower()).split()
print(line)
