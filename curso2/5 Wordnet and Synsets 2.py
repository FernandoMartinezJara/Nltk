from nltk.corpus import wordnet as wn

synSet_study = wn.synsets("study")
synSet_study

for i in range(0, 10):
    study = synSet_study[i]
    print(study)
    print(study.definition())
