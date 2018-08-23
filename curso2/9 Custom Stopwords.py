import wikipedia as wiki
from nltk.tokenize import word_tokenize

def removeStopWordsWiki(wikiSummary):

    wikiSummaryText = wiki.summary(wikiSummary)
    tokWordWiki = word_tokenize(wikiSummaryText)

    wiki_stopwords = ['a', 'and', 'are', 'as', 'be','for', 'have',
                      'in', 'is', 'of', 'or', 'that','the', 'to', 'was']
    
    wikiSummary_noSW = list()

    for i in range(0,len(tokWordWiki)):

        if tokWordWiki[i].lower() in wiki_stopwords:   # remember to make lower! 
            pass
        else:
            wikiSummary_noSW.append(tokWordWiki[i])

    return wikiSummary_noSW

mouseWiki = removeStopWordsWiki('mouse')
print(mouseWiki)
print(len(word_tokenize(wiki.summary('mouse'))))
print()
print(len(mouseWiki))
print()
print('Porcentaje reduccion {0}'.format(((411-312)/411)*100))