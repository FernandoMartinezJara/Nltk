import bs4 as bs
import urllib.request 
import nltk 
import pandas as pd
from nltk.corpus import stopwords 

response = urllib.request.urlopen('http://www.cnr.gob.cl/Ley18450/Paginas/sistema18450.aspx') 
html = response.read() 

soup = bs.BeautifulSoup(html,"lxml") 
print("\n--- Titulo ---\n")
print(soup.title.string)

print("\n--- Primer Parrafo ---\n")
print(soup.p)

print("\n--- Find todos los Parrafo ---\n")
print(soup.find_all('p'))

print("\n--- Find todos los Parrafo en loop ---\n")
for parrafo in soup.find_all('p'):
    print(parrafo.text)

print("\n--- Todo el Texto ---\n")
print(soup.get_text())

print("\n--- Todos los Link ---\n")
for link in soup.find_all('a'):
    print(link.get('href'))

print("\n--- Nav ---\n")
nav = soup.nav
print(nav)

print("\n--- Section Text ---\n")
for parrafo in soup.find_all('section', class_='body'):
    print(parrafo.text)

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

print("\n--- Tablas ---\n")
# table = soup.table
table = soup.find('table')
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

print("\n--- Tablas Con Pandas ---\n")
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
for df in dfs:
    print(df)
# text = soup.get_text(strip=True)
# tokens = [t for t in text.split()] 
# clean_tokens = tokens[:] 
# sr = stopwords.words('spanish') 

# for token in tokens: 
#     if token in stopwords.words('spanish'): 
#         clean_tokens.remove(token) 

# freq = nltk.FreqDist(clean_tokens) 

# for key,val in freq.items(): 
#     print (str(key) + ':' + str(val))

    