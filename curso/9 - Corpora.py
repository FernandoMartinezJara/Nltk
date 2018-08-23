from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

class Corpora:
    def __init__(self):
        self.corpora()

    def corpora(self):
        sample = gutenberg.raw("bible-kjv.txt")
        tokenize = sent_tokenize(sample)
        print(tokenize[5:15])

obj = Corpora()