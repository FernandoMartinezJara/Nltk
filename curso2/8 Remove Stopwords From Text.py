import wikipedia as wiki
from nltk.tokenize import word_tokenize

wiki_dog = wiki.summary('dog')
print(wiki_dog)
print()
tokWord_dog = word_tokenize(wiki_dog)
print(tokWord_dog)
print()
wikiStopWords = ['the', 'is', 'are', 'to', 'that', 'this']
wiki_dogNoSw = list()

for i in range(0, len(tokWord_dog)):
    if tokWord_dog[i].lower() in wikiStopWords:
        pass
    else:
        wiki_dogNoSw.append(tokWord_dog[i])
print(wiki_dogNoSw)
print()
print("Sin StopWords {0}, Con StopWord {1}".format(len(tokWord_dog), len(wiki_dogNoSw)))