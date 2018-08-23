from nltk.corpus import wordnet as wn

wn_awesome = wn.synsets('awesome')
print(wn_awesome)
syn_awesome = wn.synset('awesome.a.01')
print(syn_awesome)
print(syn_awesome.definition())
print(syn_awesome.examples())
print(syn_awesome.lemma_names())