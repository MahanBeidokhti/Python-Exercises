import random
import time

while True:
    num = int(input('select your number: '))
    a = random.randint(1,100)
    while True :
        if num > a :
            print("adadet bozorge")
            num = int(input('select your number: '))
        elif num < a:
            print("adadet koochike")
            num = int(input('select your number: '))
        else :
            print("pashmam dorost hads zadi")
            break
    time.sleep(2.0)
    print("haha ye dast dige :) ")
    time.sleep(1.7)
    i = input("ok? (age are begoo 'y' , age na begoo 'n'): ")
    if i == "y":
        print("eyval")
        time.sleep(1.5)
        print("pas ba in hesab")
        time.sleep(1.5)
    if i == "n":
        time.sleep(2.0)
        print("ey baba, asla be darak, bye")
        break