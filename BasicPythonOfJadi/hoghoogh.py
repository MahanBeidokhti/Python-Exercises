a = input('haji ye soal\nhar saat chand hezar toman hoghoogh migiri ? : ')
b = input('hala ye soale dige, roozi chand saat kar mikooni ? : ')

def hoghoogh(a,b):
    if int(a) >= 15 and int(b) >= 3:
        print('ya hosein, khar pooli hasti ha! \nbe har hal')
    if int(b) < 3 and int(a) < 15:
        print('zahmat keshidi, khaste nashi amooyi :/ \nbe har hal')
    if int(b) < 3 and int(a) > 15:
        print('wtf! kar ke nemikoni, pas chejoori enghadr dar miari? :/ \nbe har hal')
    jam = int(a) * int(b)
    return jam

print("to mahi " , str(int(hoghoogh(a,b)) * 30) , " hezar toman hoghoogh migiri")