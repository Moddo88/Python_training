class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def _clean_word_list(self, text):
        punctuation = [',', '.', '=', '!', '?', ';', ':', '-', '(', ')']
        for char in punctuation:
            text = text.replace(char, '')
        return text.lower().split()

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                words = self._clean_word_list(content)
                all_words[filename] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            try:
                index = words.index(word.lower())
                result[filename] = index + 1
            except ValueError:
                pass
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[filename] = count
        return result


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))     # 3 слово по счету
print(finder2.count('teXT'))    # 4 слова teXT в тексте всего
