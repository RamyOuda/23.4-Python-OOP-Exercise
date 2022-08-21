"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """
        Finds a word from an external list of words

        >>> test = WordFinder("words.txt")
        235886 words read.

        >>> test.random() in [word.strip() for word in open("words.txt")]
        True

    """

    def __init__(self, file):
        """
            declare 'self.words' as a list of words found in an external file
            print the number of words in the 'self.words' list
        """
        self.words = [word.strip() for word in open(file)]
        print(f"{len(self.words)} words read.")

    def __repr__(self):
        """ Show representation """
        return f"<SerialGenerator words = {self.words}>"

    def random(self):
        """ Return a random word from the list """
        return random.choice(self.words)
