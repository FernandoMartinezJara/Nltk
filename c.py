from nltk.corpus import wordnet 
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("alto"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer() 
print(stemmer.stem('running\n'))

from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)

from nltk.stem import SnowballStemmer
french_stemmer = SnowballStemmer('spanish')
print(french_stemmer.stem("hablando\b"))

from nltk.stem import PorterStemmer 
stemmer = PorterStemmer() 
print(stemmer.stem('increases\b'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases\n'))

from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer 
stemmer = PorterStemmer() 
lemmatizer = WordNetLemmatizer() 
print(stemmer.stem('stones')) 
print(stemmer.stem('speaking')) 
print(stemmer.stem('bedroom')) 
print(stemmer.stem('jokes')) 
print(stemmer.stem('lisa')) 
print(stemmer.stem('purple')) 
print('----------------------') 
print(lemmatizer.lemmatize('stones')) 
print(lemmatizer.lemmatize('speaking'))
print(lemmatizer.lemmatize('bedroom'))
print(lemmatizer.lemmatize('jokes'))
print(lemmatizer.lemmatize('lisa'))
print(lemmatizer.lemmatize('purple'))