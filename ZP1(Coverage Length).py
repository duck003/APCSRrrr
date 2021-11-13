a = int(input())

total = 0

for i in range(a):
    b = [int(x) for x in input().split()]
    total += b[1] - b[0]

print(total)
