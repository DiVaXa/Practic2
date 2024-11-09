class WordsFinder:

    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        l = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punc:
                        line = line.replace(i, '')
                l = l + line
            all_words.update({self.file_names: l.split()})
        return all_words

    def find(self, word):
        word = word.lower()
        found_words = {}
        for file_name, words in self.get_all_words().items():
            found = False
            for i in range(len(words)):
                if words[i] == word:
                    found = True
                    break
            if found:
                found_words[file_name] = i + 1
        return found_words


    def count(self, word):
        word = word.lower()
        word_number = {}
        for file_name, words in self.get_all_words().items():
            word_number[file_name] = words.count(word)
        return word_number

if __name__ == '__main__':

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

