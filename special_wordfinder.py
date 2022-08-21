from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """
        Alternate word finder that ignores # and blank lines

        >>> swf = SpecialWordFinder("words.txt")
        235886 words read.
    """

    def parse(self, file):
        """ Returns a list of words from 'file' that do not start with '#' """
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]
