from nltk.corpus import wordnet

class Wordnet:
    def __init__(self):
        self.wordnet()
        self.similarity()

    def wordnet(self):
        syns = wordnet.synsets("program")

        # synsets
        print("Synsets")
        print(syns)
        print("\n")

        # just the word
        print("just the word")
        print(syns[0].name())
        print("\n")

        # definition
        print("definition")
        print(syns[0].definition())
        print("\n")

        # examples
        print("examples")
        print(syns[0].examples())
        print("\n")

        synonyms = []
        antonyms = []

       
        for syn in wordnet.synsets("good"):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        
        print("synonyms")
        print(set(synonyms))
        print("\n")

        print("antonyms")
        print(set(antonyms))

    def similarity(self):
        print("\nSimilarity")
        w1 = wordnet.synset("ship.n.01")
        w2 = wordnet.synset("boat.n.01")
        print(w1.wup_similarity(w2))

obj = Wordnet()