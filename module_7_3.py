def remove_double_list(double_list):
    one_list = []
    for i in double_list:
        for j in i:
            one_list.append(j)
    return one_list


def remove_punctuation(line):
    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
    for i in punctuation:
        for char in line:
            if char == i:
                line = line.replace(char, '')
    return line


class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i,encoding='utf-8') as file:
                line = remove_punctuation((file.read().lower()).split())
                all_words[i] = line
        return all_words

    def find(self, word):
        word_lower = word.lower()
        all_words = self.get_all_words()
        slovar = {}
        for name, words in all_words.items():
            if word_lower in words:
                slovar[name] = words.index(word_lower) + 1
        return slovar

    def count(self, word):
        word_lower = word.lower()
        all_words = self.get_all_words()
        slovar = {}
        for name, words in all_words.items():
            if word_lower in words:
                slovar[name] = words.count(word_lower)
        return slovar





finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего