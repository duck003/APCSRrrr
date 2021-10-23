rows, cols, cops = [int(x) for x in input().split()]

n = []
c = []

for i in range (rows):
    n.append([int(x) for x in input().split()])

c = [int(x) for x in input().split()]
c.reverse()

def rotate(x):

    y = []
    rows = len(x)
    cols = len(x[0])
    rowsoy = cols
    colsoy = rows

    for i in range(rowsoy):
        r = []
        for j in range(colsoy):
            r.append(x[j][-i-1])
        y.append(r)
    return y

for x in c:
    if x == 1:
        n.reverse()
    else:   
        n = rotate(n)
        
print(len(n),len(n[0]))
for rows in n:
    print(*rows)
