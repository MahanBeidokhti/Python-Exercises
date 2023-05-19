#اینجوری کار میکنه که چند تا عدد بهش میدی ، و به محض اینکه عدد -1 رو بهش بدی میانگین اعداد رو اعلام میکنه
a = int(input('add a number: '))
i = 0
b = 1
while b != -1:
    b = int(input('add another number: '))
    a = a + b
    i += 1
miangin = a / i 
print('miangin adad ha mishe: ' , miangin)