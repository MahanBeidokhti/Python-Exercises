class info_graphy:
    dict1 = dict()
    dict2 = dict()
    dict3 = dict()
    def __init__(self, name , vazn , ghad , sen):
        self.dict1[name] = ghad
        self.dict2[name] = vazn
        self.dict3[name] = sen
    def printinf(self):
        print(' there are totaly %i people: ' % len(self.dict1))
        for each in list(self.dict1.keys()):
            print("""%s's info:
            ghad : %s cm
            vazn : %s Kg
            sen  : %s sal""" % (each , self.dict1[each], self.dict2[each], self.dict3[each]))
   
         
print("This is the info-graphy machine! each time , you have to enter the name you want, then you shloud enter his vazn and ghad and sen")
a = ''
while a != 'finish' :
    a = ''
    infos = info_graphy(input('enter the name : ') , input('vazn : ') , input('ghad : ') , input('sen : '))
    while a != 'add' and a != 'finish':
        a = input('wanna add another one or you want to finish ? ("add" or "finish") : ')
        if a != 'add' and a != 'finish':
            print('please just write "add" or "finish"!')

infos.printinf()