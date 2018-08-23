from nltk.book import *

text1

type(text1)

MD_book = text1

MD_book[0:50]

len(MD_book)

MD_book.concordance("whale")

MD_book.similar("whale")

wsj = text7

wsj.concordance("money")

IM_chat = text5
IM_chat.concordance("sex")

press_speech = text4
press_speech.common_contexts(["united", "states"])
press_speech.similar("united")
press_speech.common_contexts(["justice", "people"])
press_speech.common_contexts(["justice"])
press_speech.similar("justice")