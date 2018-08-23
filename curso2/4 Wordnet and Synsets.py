from nltk.corpus import wordnet as wn

wn_meditation = wn.synsets('meditation')
wn_meditation

meditation01 = wn.synset('meditation.n.01')
meditation01
meditation01.definition()

meditation02 = wn.synset('meditation.n.02')
meditation02
meditation02.definition()