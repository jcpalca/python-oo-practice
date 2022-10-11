from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

        >>> wf = WordFinder()
        3 words read

        >>> wf.random()
        'cat'

        >>> wf.random()
        'cat'

        >>> wf.random()
        'porcupine'

        >>> wf.random()
        'dog'

    """

    def __init__(self, file_path='words.txt'):
        self.file_path = file_path
        self.file = open(file_path)
        self.words_list = []
        for line in self.file:
            self.words_list.append(line.strip())
        print(f"{len(self.words_list)} words read")


    def random(self):
        return choice(self.words_list)
