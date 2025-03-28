import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    cleaned_line = re.sub(r'[,\.\=\!\?\;\:\s-]', ' ', line.lower())
                    words.extend(cleaned_line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            words_count = words.count(word.lower())
            result[file_name] = words_count

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
