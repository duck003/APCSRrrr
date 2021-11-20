from time import perf_counter

n, m, k = [int(x) for x in input().split() ]
start = perf_counter()

players = [x+1 for x in range(n)]
for out in range(k):   
    players = players[m:] + players[:m-1]
print(players[0])

stop = perf_counter()
print('time:',stop - start)
