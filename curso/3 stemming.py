from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

class Stemming():

    ps = PorterStemmer()
    ls = LancasterStemmer()

    def __init__(self):
        self.stemmingArray()
        print()
        self.stemmingText()

    def stemmingArray(self):
        words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
        for word in words:
            print(self.ps.stem(word))

    def stemmingText(self):
        text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least"
        words = word_tokenize(text)
        print("Porter Stemmer")
        #for word in words:
        #    print(self.ps.stem(word))
        [self.ps.stem(t) for t in words]
        # print("\n")

obj = Stemming()