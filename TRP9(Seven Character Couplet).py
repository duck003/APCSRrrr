z = int(input())
sen = []
result = []
for i in range(z):
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    sen.append(a)
    sen.append(b)
    AR = False
    BR = False
    CR = False
    if (a[1] != a[3] and a[1] == a[5]) and (b[1] != b[3] and b[1] == b[5]): 
        AR = True
    if a[-1] == 1 and b[-1] == 0:
        BR = True
    if a[1] != b[1] and a[3] != b[3] and a[5] != b[5]:
        CR = True

    if AR == True and BR == True and CR == True:
        result.append("None")
    else:
        r = ""
        if AR == False:
            r += "A"
        if BR == False:
            r += "B"   
        if CR == False:
            r += "C"
        result.append(r)

for r in result:
    print(r)
