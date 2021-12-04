z = int(input())
sen = []

for i in range(z*2):
    a = [int(x) for x in input().split()]
    sen.append(a)

for i in range(0, z*2, 2):
    AR = False
    BR = False
    CR = False
    if sen[i][1] != sen[i][3] and sen[i][1] == sen[i][5] and sen[i+1][1] != sen[i+1][3] and sen[i+1][1] == sen[i+1][5]: 
        AR = True
    if sen[i][-1] == 1 and sen[i+1][-1] == 0:
        BR = True
    if sen[i][1] != sen[i+1][1] and sen[i][3] != sen[i+1][3] and sen[i][5] != sen[i+1][5]:
        CR = True

    if AR == True and BR == True and CR == True:
        print("None")
    else:
        a = ''
        if AR == False:
            a += "A"
        if BR == False:
            a += "B"   
        if CR == False:
            a += "C"
        print(a)
       
