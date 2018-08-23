from nltk.stem import WordNetLemmatizer

class Lemmatizing:

    lemmatizer = WordNetLemmatizer()

    def __init__(self):
        self.lemmatizing()

    def lemmatizing(self):
        print(self.lemmatizer.lemmatize("cats"))
        print(self.lemmatizer.lemmatize("cacti"))
        print(self.lemmatizer.lemmatize("geese"))
        print(self.lemmatizer.lemmatize("rocks"))
        print(self.lemmatizer.lemmatize("python"))
        print(self.lemmatizer.lemmatize("better", pos="a"))
        print(self.lemmatizer.lemmatize("best", pos="a"))
        print(self.lemmatizer.lemmatize("run"))
        print(self.lemmatizer.lemmatize("run", pos="v"))

obj = Lemmatizing()