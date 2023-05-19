import random
for i in range (0,2):

    while True :
        num = random.randint(1,10)
        #   num = int(input("what is your number ? : \n"))
        if num == 1 :
            print(""". . . . .
. . . . . 
. . o . .
. . . . .
. . . . .\n""")
            break
        if num == 2 :
            print(""". . . . .
. . . o .
. . . . .
. o . . .
. . . . .\n""")
            break
        if num == 3 : 
            print(""". . . . .
. . . o .
. . o . .
. o . . .
. . . . .\n""")
            break
        if num == 4 : 
            print(""". . . . .
. o . o .
. . . . .
. o . o .
. . . . .\n""")
            break
        if num == 5 : 
            print(""". . . . .
. o . o .
. . o . .
. o . o .
. . . . .\n""")
            break
        if num ==  6 : 
            print(""". . . . .
. o . o .
. o . o .
. o . o .
. . . . .\n""")
            break
        if num < 1 or num > 6:
            print("%s is out of range.\n" %num)

print("\nfinish!")