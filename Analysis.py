import sys
import nltk

# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords

# nltk.download()

#text = "Hello Mr. Smith, how are you doing today? The weather is great an python is awesome, The sky is pinkish-blue. You should not eat cardboard"
#print(sent_tokenize(text))
# print()
# print(word_tokenize(text))
# for i in word_tokenize(text):
#     print(i)

# stops = set(stopwords.words('spanish'))

# for word in stops:
#     print(word)
 
# text = 'In this tutorial, I\'m learning NLTK. It is an interesting platform.'
# stop_words = set(stopwords.words('english'))
# words = word_tokenize(text)
 

# new_sentence = []
# for word in words:
#     if word not in stop_words:
#         new_sentence.append(word)
# print(new_sentence)

# with open('NLTK.txt', "r", encoding="latin-1") as file:
#     read_file = file.read()
#     text = nltk.Text(nltk.word_tokenize(read_file))
#     match = text.concordance('language')

# gutenberg_files = nltk.corpus.gutenberg.fileids()
# print(gutenberg_files)
# bryant_words = nltk.corpus.gutenberg.words('bryant-stories.txt')
# print(len(bryant_words))

import random
print(random.random())