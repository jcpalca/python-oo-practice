from random import choice

class WordFinder:
    """ Word Finder: finds random words from a dictionary.

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
        """ reads the file
            reports the number of words read
            closes the file
        """
        self.file_path = file_path
        self.file = open(file_path)
        self.words_list = self.read_lines(self.file)

        print(f"{len(self.words_list)} words read")

        self.file.close()

    def __repr__(self):
        """ represents the word finder instance 
            includes the file path, first three words, # of words in list
        """
        return f"""<{self.__class__.__name__}
            file_path={self.file_path} 
            first_three_words={self.words_list[0:3:]}
            num_words={len(self.words_list)}
        >"""

    def random(self):
        """ returns a random element from words list
        """
        return choice(self.words_list)

    def read_lines(self, open_file):
        """ reads the file and strips "\\n" character
            returns a list of words from file
        """
        return [word.strip() for word in open_file]

class SpecialWordFinder(WordFinder):
    """ Special word finder that filters out #comments and empty lines

        >>> swf = SpecialWordFinder("foods.txt")
        4 words read

        >>> swf.random()
        'apple'

        >>> swf.random()
        'mango'

        >>> swf.random()
        'kale'

        >>> swf.random()
        'parsnips'

    """

    # def __init__(self, file_path):
    #     super().__init__(file_path)
        
    def read_lines(self, open_file):
        """ filters out empty lines and comments from the parent's list of words
            return a new filtered list
        """
        return [word for word in super().read_lines(open_file) 
                if not word.startswith("#") and not word == ""]
    

    

    
