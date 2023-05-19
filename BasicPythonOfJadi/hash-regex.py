import hashlib
import re

dict1 = {}
dict2 = {}

for lim in range (10000):
    dict1[hashlib.sha256(str(lim).encode()).hexdigest()] = lim

with open('D:\mahan\Programming\Mine\jadi\hashed files and nums - Regex.csv') as lst:
    lines = lst.readlines()
    for i in lines:
        dict2[re.findall(r'(.*)\,',i)[0]] = re.findall(r'\,(.*)',i)[0].strip()
print(dict1[dict2[input('enter the name : ')]])