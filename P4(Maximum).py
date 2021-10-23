rows, cols= [int(x) for x in input().split()]

y = []
maxn = []

for i in range(rows):
    maxn.append( max([int(x) for x in input().split()] ))

z = sum(maxn)
print(z)

for n in maxn:
    if z % n == 0:
        y.append(n)

if y:
    print(*y)
else:
    print(-1)
