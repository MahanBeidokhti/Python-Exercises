from ast import Lambda
import csv
from operator import itemgetter
dict1 = {}
with open('D:\mahan\Programming\jadi\grade.csv') as file:
    listt = csv.reader(file)
    for line in listt:
        name = line[0]
        grade = line[1:]
        all_nums = 0.0
        counter = 0
        for num in grade:
            counter += 1 
            all_nums += float(num)
        mean = all_nums / counter
        dict1[name] = mean
        #print("%10s's mean is : %s" % (line[0] , mean))
    members = list(dict1.items())
    members.sort(key=lambda x:x[1], reverse=True)
    count = 0
    for (esm,num) in members:
        count += 1
        print('%s. %6s : %2.2f' % (count , esm , num ))