import re

string = '555-123-5675 555.456.2344 worker-bee@gmail.com TedMikeTed@mail.com'

findString = re.search(r'Ted', string).group()
print(findString)
print()

findString = re.findall(r'Ted', string)
print(findString)
print()

findString = re.findall(r'\w+', string)
print(findString)
print()

findString = re.findall(r'[a-z]+', string)
print(findString)
print()

findString = re.findall(r'[A-Z]+', string)
print(findString)
print()

findString = re.findall(r'[0-9]+', string)
print(findString)
print()

findString = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d+', string)
print(findString)
print()

findString = re.findall(r'\d\d\d.\d\d\d.\d\d\d\d+', string)
print(findString)
print()

findString = re.findall(r'\d\d\d\.\d\d\d\.\d\d\d\d+', string)
print(findString)
print()

findString = re.findall(r'\d\d\d[.]d\d\d[.]\d\d\d\d+', string)
print(findString)
print()

findString = re.findall(r'\d\d\d[.]\d\d\d[.]\d\d\d\d+', string)
print(findString)
print()

findString = re.findall(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d+', string)
print(findString)
print()

findString = re.findall(r'\w+@+\w+.com', string)
print(findString)
print()

findString = re.findall(r'[\w-]+@+\w+.com', string)
print(findString)
print()

findString = re.findall(r'[\w$@-]+@+\w+.com', string)
print(findString)
print()