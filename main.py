import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                words_list = []
                for line in f:
                    line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words_list.extend(line.split())
                    all_words[file_name] = words_list
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result

file_name = 'test_file.txt'
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
