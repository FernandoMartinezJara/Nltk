from nltk.tokenize import sent_tokenize, word_tokenize

class Tokenizing:        
    
    def __init__(self):
        self.sentTokenizing()
        self.wordTokenizing()

    def sentTokenizing(self):
        example = "Hello Mr. Smith, how are you doing today? the weather is great and python is awesome. " \
        + "the sky is pinkish-blue. You should no eat cardboard"
        print(sent_tokenize(example))
        print()
    
    def wordTokenizing(self):
        example = "Hello Mr. Smith, how are you doing today? the weather is great and python is awesome. " \
        + "the sky is pinkish-blue. You should no eat cardboard"
        print(word_tokenize(example))
        

obj = Tokenizing()