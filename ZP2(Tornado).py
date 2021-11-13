z = int(input())
x = int(input())
c = []
v = 0
number = 0

for i in range(z):
    b = [int(x) for x in input().split()]
    c.append(b)

i = j = z//2
a = [c[i][j]]

ttt = "lurrddll"  
ftf = "lurrddllluuurrrrddddllll"    

for k in range(z**2-1):
    if ttt[k] == "l":
        j = j-1
    elif ttt[k] == "u":
        i = i-1
    elif ttt[k] == "r":
        j = j+1
    elif ttt[k] == "d":
        i = i+1
    a.append(c[i][j])
    
print(*a,sep="")
