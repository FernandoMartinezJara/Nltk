import wikipedia as wiki
import re

sample = wiki.summary('smile')
print(sample)
print()
sampleNoP = re.findall(r'\w+', sample)
print(sampleNoP)
print()
sample = wiki.summary('bird')
sampleNoP = re.findall(r'\w+bird', sample)
print(sampleNoP)
print()
sampleNoP = re.findall(r'bird+\w', sample)
print(sampleNoP)