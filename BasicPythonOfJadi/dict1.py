dic = {'c1': 'Red', 'c2': 'Green', 'c3': None}
dic = {key:value for (key, value) in dic.items() if value is not None}
print(dic)