a = 2
b = 2
counter=0
lim = int(input("how much you want to count? : "))
while b <= lim:
    a = str(a) + str(b)
    b = b + 2
for charracter in a:
    if int(charracter)%2==1:
        counter += 1
    print('%s num till now, the last num is %s' % (counter , charracter))
print(counter, ' is the final count!')