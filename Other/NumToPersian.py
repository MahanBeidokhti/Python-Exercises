num = int(input(""))

flag = 0
flag2 = 0
flag3 = 0
numstr = ""

if num == 10000000:
    numstr = numstr + "ده میلیون"
    
ragham = int(num/(10**6)%10)
if ragham!=0:
    if ragham==1:
        numstr = numstr + "یک "
    if ragham==2:
        numstr = numstr + "دو "
    if ragham==3:
        numstr = numstr + "سه "
    if ragham==4:
        numstr = numstr + "چهار "
    if ragham==5:
        numstr = numstr + "پنج "
    if ragham==6:
        numstr = numstr + "شش "
    if ragham==7:
        numstr = numstr + "هفت "
    if ragham==8:
        numstr = numstr + "هشت "
    if ragham==9:
        numstr = numstr + "نه "
    numstr = numstr + "میلیون "
    flag+=1

ragham = int((num/(10**5))%10)
if ragham!=0:
    
    if flag == 1:
        numstr = numstr + "و "
    else:
        flag=1
    
    if ragham==1:
        numstr = numstr + "صد "
    elif ragham==2:
        numstr = numstr + "دویست "
    elif ragham==3:
        numstr = numstr + "سیصد "
    else:
        if ragham==4:
            numstr = numstr + "چهار "
        if ragham==5:
            numstr = numstr + "پنج "
        if ragham==6:
            numstr = numstr + "شش "
        if ragham==7:
            numstr = numstr + "هفت "
        if ragham==8:
            numstr = numstr + "هشت "
        if ragham==9:
            numstr = numstr + "نه "
        numstr = numstr + "صد "
    flag2 = 1

ragham = int((num/(10**4))%10)
if ragham!=0:
    
    if flag == 1:
        numstr = numstr + "و "
    else:
        flag=1

    if ragham==1:
        flag3 = 1
        ragham2 = int((num/(10**3))%10)
        if ragham2 == 0:
            numstr = numstr + "ده "
        if ragham2 == 1:
            numstr = numstr + "یازده "
        if ragham2 == 2:
            numstr = numstr + "دوازده "
        if ragham2 == 3:
            numstr = numstr + "سیزده "
        if ragham2 == 4:
            numstr = numstr + "چهارده "
        if ragham2 == 5:
            numstr = numstr + "پانزده "
        if ragham2 == 6:
            numstr = numstr + "شانزده "
        if ragham2 == 7:
            numstr = numstr + "هفده "
        if ragham2 == 8:
            numstr = numstr + "هجده "
        if ragham2 == 9:
            numstr = numstr + "نوزده "
    else:
        if ragham==2:
            numstr = numstr + "بیست "
        if ragham==3:
            numstr = numstr + "سی "
        if ragham==4:
            numstr = numstr + "چهل "
        if ragham==5:
            numstr = numstr + "پنجاه "
        if ragham==6:
            numstr = numstr + "شصت "
        if ragham==7:
            numstr = numstr + "هفتاد "
        if ragham==8:
            numstr = numstr + "هشتاد "
        if ragham==9:
            numstr = numstr + "نود "
    
    flag2 = 1

ragham = int((num/(10**3))%10)
if ragham!=0:
    
    if flag3 != 1:
        
        if flag == 1:
            numstr = numstr + "و "
        else:
            flag=1
    
        if ragham==1:
            numstr = numstr + "یک "
        if ragham==2:
            numstr = numstr + "دو "
        if ragham==3:
            numstr = numstr + "سه "
        if ragham==4:
            numstr = numstr + "چهار "
        if ragham==5:
            numstr = numstr + "پنج "
        if ragham==6:
            numstr = numstr + "شش "
        if ragham==7:
            numstr = numstr + "هفت "
        if ragham==8:
            numstr = numstr + "هشت "
        if ragham==9:
            numstr = numstr + "نه "
        flag2 = 1
    

if flag2==1:
    numstr = numstr + "هزار "
    
ragham = int((num/(10**2))%10)
if ragham != 0:
    
    if flag == 1:
        numstr = numstr + "و "
    else:
        flag=1
    
    if ragham==1:
        numstr = numstr + "صد "
    elif ragham==2:
        numstr = numstr + "دویست "
    elif ragham==3:
        numstr = numstr + "سیصد "
    else:
        if ragham==4:
            numstr = numstr + "چهار "
        if ragham==5:
            numstr = numstr + "پنج "
        if ragham==6:
            numstr = numstr + "شش "
        if ragham==7:
            numstr = numstr + "هفت "
        if ragham==8:
            numstr = numstr + "هشت "
        if ragham==9:
            numstr = numstr + "نه "
        numstr = numstr + "صد "


ragham = int((num/10)%10)
flag3 = 0
if ragham!=0:
    
    if flag == 1:
        numstr = numstr + "و "
    else:
        flag=1
    
    if ragham==1:
        flag3 = 1
        ragham2 = num%10
        if ragham2 == 0:
            numstr = numstr + "ده "
        if ragham2 == 1:
            numstr = numstr + "یازده "
        if ragham2 == 2:
            numstr = numstr + "دوازده "
        if ragham2 == 3:
            numstr = numstr + "سیزده "
        if ragham2 == 4:
            numstr = numstr + "چهارده "
        if ragham2 == 5:
            numstr = numstr + "پانزده "
        if ragham2 == 6:
            numstr = numstr + "شانزده "
        if ragham2 == 7:
            numstr = numstr + "هفده "
        if ragham2 == 8:
            numstr = numstr + "هجده "
        if ragham2 == 9:
            numstr = numstr + "نوزده "
    else:
        if ragham==2:
            numstr = numstr + "بیست "
        if ragham==3:
            numstr = numstr + "سی "
        if ragham==4:
            numstr = numstr + "چهل "
        if ragham==5:
            numstr = numstr + "پنجاه "
        if ragham==6:
            numstr = numstr + "شصت "
        if ragham==7:
            numstr = numstr + "هفتاد "
        if ragham==8:
            numstr = numstr + "هشتاد "
        if ragham==9:
            numstr = numstr + "نود "
    
ragham = num%10
if ragham!=0:
    
    if flag3 != 1:
        
        if flag == 1:
            numstr = numstr + "و "
        else:
            flag=1
    
        if ragham==1:
            numstr = numstr + "یک "
        if ragham==2:
            numstr = numstr + "دو "
        if ragham==3:
            numstr = numstr + "سه "
        if ragham==4:
            numstr = numstr + "چهار "
        if ragham==5:
            numstr = numstr + "پنج "
        if ragham==6:
            numstr = numstr + "شش "
        if ragham==7:
            numstr = numstr + "هفت "
        if ragham==8:
            numstr = numstr + "هشت "
        if ragham==9:
            numstr = numstr + "نه "   

print(numstr)