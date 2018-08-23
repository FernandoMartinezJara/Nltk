from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class StopWords:
    def __init__(self):

        self.showStopWords()
        print()
        self.stopWordsRefactor()

    def showStopWords(self):
        stop_words = set(stopwords.words("english"))
        print(stop_words)

    def stopWords(self):
        stop_words = set(stopwords.words("english"))
        text = "This is an example showing off stop word filtration."
        words = word_tokenize(text)
        filtered_sentence = []
        for word in words:
            if word not in stop_words:
                filtered_sentence.append(word)
        print(filtered_sentence)
    
    def stopWordsRefactor(self):
        stop_words = set(stopwords.words("english"))
        text = "This is an example showing off stop word filtration."
        words = word_tokenize(text)
        filtered_sentence = [word for word in words if not word in stop_words]
        print (filtered_sentence)

obj = StopWords()