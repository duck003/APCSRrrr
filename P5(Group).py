z = int(input())
people = [int(x) for x in input().split()]

groups = 0
index = 0
yep = []

while index < z:
    if people[index] in yep:
        index += 1
        if not index in yep:
            groups += 1
    else:
        yep.append(people[index])
        index = people[index]

        
print(groups)
