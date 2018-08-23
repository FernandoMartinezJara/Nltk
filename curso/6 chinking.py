import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

class Chinking():
    train_text = state_union.raw("2005-GWBush.txt")
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

    sample_text = state_union.raw("2006-GWBush.txt")
    tokenized = custom_sent_tokenizer.tokenize(sample_text)

    def __init__(self):
        self.chuncking()
    
    def chuncking(self):
        try:
            for i in self.tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                chunkGram = r"""chunk: {<.>+}
                                        }<VB.?|IN|DT|TO>+{"""
                chunkParser = nltk.RegexpParser(chunkGram)
                chunked = chunkParser.parse(tagged)
                print(chunked)
        except Exception as e:
            print(str(e))

obj = Chinking()