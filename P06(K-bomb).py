n, m, k = [int(x) for x in input().split() ]

players = [x+1 for x in range(n)]
listw = players
out = 0

while out < k:
    for i in range(m):
        if i+1 == m:
            listw = listw[i+1:] + listw [:i]
            out += 1

print(listw[0])
