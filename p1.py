a = input()
x = 0
y = 0 
z = 60

grades = [int(i) for i in input().split()]
grades.sort()
print (*grades)

gnotpass = []
gpass= []

for i in range(len(grades)):
    if grades[i] < z:
        gnotpass.append(grades[i])

if grades[0] >= 60:
    print("best case")

else:
   for i in range(len(grades)):
       if grades[i] < 60:
           gnotpass.append(grades[i])
   print(gnotpass[-1])

if grades[-1] < 60:
    print("worst case")

else:
   for i in range(len(grades)):
       if grades[i] >= 60:
           gpass.append(grades[i])
   print(gpass[0])



        

