import time
import random
print('consider a number between 1 and 100 in your mind!')
time.sleep(4.0) 
print("OK!")
time.sleep(1.2)
print("are you ready ?") 
time.sleep(1.2)
print("lets go!")
print("""if my number was bigger than yours, say '-'
      if it was smaller, say '+'
      and if it was your number say 'yes'!""")
time.sleep(5)
while True: 
    min , max = 1 , 100
    hads = random.randint(min,max)
    print(hads, "is your number ? :") 
    reaction = input("'yes' or '+' or '-' : ")
    while reaction != "yes":
        if max - min < 1 :
            print("please check again, your number is ", hads ,"?")
            reaction = input("('yes' or 'no'): ")
            break
        if reaction == "-":
            max = hads -1
            hads = random.randint(min,max)
        elif reaction == "+":
            min = hads + 1
            hads = random.randint(min,max)
        print(hads, " is your number ? :")
        reaction = input("")
    if reaction=="yes":
        print("really 😍?")
        time.sleep(1.5)
        print("heh😎😏! damn it feel good to be a gangsta!")
        time.sleep(1.2)
        print("anyway! wanna play again ?")
    if reaction == "no":
        print("hmmmm , i think something is wrong!")
        time.sleep(2.0)
        print("wanna try again? :")
    play_again = input("('yes' or 'no') : ")
    if play_again == "no":
        break
    if play_again == "yes":
        print("so, consider a number beetwen 1 and 100 in your mind again!")
        time.sleep(3.0)
        print("ok")
print("ok! see you later!")
time.sleep(2.0)