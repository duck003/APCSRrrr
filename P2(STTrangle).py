a, b, c = input().split()

length = []
length.append(int(a))
length.append(int(b))
length.append(int(c))

length.sort()

print(*length)

if length[0] + length[1] < length[2]:
    print("No") 
elif length[0]**2 + length[1]**2 < length[2]**2:
    print("Obtuse") 
elif length[0]**2 + length[1]**2 == length[2]**2:
    print("Right")
elif length[0]**2 + length[1]**2 > length[2]**2:
    print("Acute")     
