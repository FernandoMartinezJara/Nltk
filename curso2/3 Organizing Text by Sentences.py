from nltk.corpus import gutenberg

#Lista de archivos en corpus Gutenberg
gutenberg.fileids()

BlakePoems = gutenberg.sents("blake-poems.txt")

BlakePoems[40]
BlakePoems[40][3]

len(BlakePoems)

for i in range(0,len(BlakePoems)):
    if len(BlakePoems[i]) == 10:
        print(BlakePoems[i])
