import random

class WordFinder:
    """ Word Finder: finds random words from a dictionary. """
    def __init__(self, path):
        """ Constructor for WordFinder """
        self.file = open(path, "r")
        self.words = self.getAllWords()

    def getAllWords(self):
        """ Retrieves all words from a file """
        return [line.strip() for line in self.file.readlines()]

    def random(self):
        """ Returns a random word from the file """
        return self.words[random.randrange(0, len(self.words))]
        
class SpecialWordFinder(WordFinder):
    """ Special Word Finder: finds random words from a dictionary not including spaces and # """
    def __init__(self, path):
        """ Constructor for SpecialWordFinder """
        super().__init__(path)

    def getAllWords(self):
        """ Retrieves all words from a file (not reading spaces and anything starts with '#' """
        return [line.strip() for line in self.file.readlines() if line.strip() != "" and not line.startswith("#")]
