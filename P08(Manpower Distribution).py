a, b, c = [int(x) for x in input().split()]
d, e, f = [int(x) for x in input().split()]
z = int(input())
large = -10000000000

for i in range(z+1):
    o = i
    r = z-i
    q = a*(o**2) + b*o + c
    w = d*(r**2) + e*r + f
    total = q + w 
    if total > large:
        large = total

print(large)
