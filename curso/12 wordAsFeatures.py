import nltk
import random
from nltk.corpus import movie_reviews

class WordAsFeatures:
    
    word_features = {}

    documents = [(list(movie_reviews.words(fileid)), category) 
                for category in movie_reviews.categories() 
                for fileid in movie_reviews.fileids(category)]

    def __init__(self):
        self.wordAsFeatures()

    def wordAsFeatures(self):
                    
        random.shuffle(self.documents)

        all_words = []

        for w in movie_reviews.words():
            all_words.append(w.lower())
        
        all_words = nltk.FreqDist(all_words)

        self.word_features = list(all_words.keys())[:3000]
    
    def find_features(self, document):
        words = set(document)
        features = {}
        for w in self.word_features:
           features[w] = (w in words)
        return features

obj = WordAsFeatures()
print((obj.find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featureset = [(obj.find_features(rev), category) for (rev, category) in obj.documents]
