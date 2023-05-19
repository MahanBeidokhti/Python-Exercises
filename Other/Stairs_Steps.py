numbers = input()
num_list = numbers.split(" ")
s1 = int(num_list[0])
s2 = s1
x = int(num_list[1])
y = int(num_list[2])

flag = flago = 0

while s1 > 0 and s2 > 0:
    if s1 % x == 0:
        flag = 1
        break
    if s1 % y == 0:
        flag = 2
        break
    if s2 % x == 0:
        flago = 3
        break
    if s2 % y == 0:
        flago = 4
        break
    if flag == 1:
        a = s1/x
    if flag == 2:
        a = s1/y
    if flago == 3:
        b = s2/x
    if flago == 4:
        b = s2/y
    if flag & flago:
        print(b + " ta " + x + " ya " + y + " va " + a + "ta" + x + "ya" + y)
    s1 -= x
    s2 -= y

if flag:
    print("Possible!")
else:
    print("Not Possible!")
