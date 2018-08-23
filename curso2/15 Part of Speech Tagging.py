import nltk
from nltk.tokenize import word_tokenize
import wikipedia as wiki

albert = wiki.summary('Albert Einstein')
albert_tok = word_tokenize(albert)
al_sample = albert_tok[0:50]
print(al_sample)
print()
al_sample_POS = nltk.pos_tag(al_sample)
print(al_sample_POS)
print()
print(nltk.help.upenn_tagset('NNS'))
print()

for i in range(0, len(al_sample_POS)):
    if al_sample_POS[i][1] == 'NNP':
        print(al_sample_POS[i][0])