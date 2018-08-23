import nltk
import random
from nltk.corpus import movie_reviews

class TextClassification:
    def __init__(self):
        self.textClassification()

    def textClassification(self):

        documents = [(list(movie_reviews.words(fileid)), category) 
                    for category in movie_reviews.categories() 
                    for fileid in movie_reviews.fileids(category)]
                    
        random.shuffle(documents)

        all_words = []

        for w in movie_reviews.words():
            all_words.append(w.lower())
        
        all_words = nltk.FreqDist(all_words)
        print(all_words.most_common(15))


obj = TextClassification()