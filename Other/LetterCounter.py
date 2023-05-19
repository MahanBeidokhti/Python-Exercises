string = input("give me some words ; i'll count the letters for you : ")

dic = dict()

for letter in string:
    dic[letter] = dic.get(letter , 0) + 1
    
for letter_counts in list(dic.keys()):
    print('%s came %s times in your string!' % (letter_counts , dic[letter_counts]))