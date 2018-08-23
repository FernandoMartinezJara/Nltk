from nltk.compat import gutenberg

gutenberg.fileids()

dir(gutenberg)

JM_book = gutenberg.words('milton-paradise.txt')
len(JM_book)

sample_JM = JM_book[100:150]
sample_JM
len(sample_JM)

set_JM = set(sample_JM)
set_JM
len(set(set_JM))
type(set_JM)
sorteSet_JM = sorted(set_JM)
sorteSet_JM
len(sorteSet_JM)

print("milton-paradise.txt has: ", len(JM_book))
len(set(JM_book))