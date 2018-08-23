from nltk.tokenize import word_tokenize
import wikipedia as wiki
from nltk.probability import FreqDist

camara = wiki.summary('camera')
camara = word_tokenize(camara)

fDist_camera = FreqDist(camara)
print(fDist_camera.most_common(10))
print()
bird = wiki.summary('bird')
bird = word_tokenize(bird)
fDist_bird = FreqDist(bird)
print(fDist_bird.most_common(10))
print()
language = wiki.summary('language')
language = word_tokenize(language)
fDist_language = FreqDist(language)
print(fDist_language.most_common(10))

