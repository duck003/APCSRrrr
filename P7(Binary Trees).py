from typing import List
z = int(input()) 


class Node():

    def __init__(self):
        self.is_root = True
        self.children:List[Node] = []

x:List[Node] = []

for i in range(z):
    x.append(Node())

for i in range(z):
    a = [int(x) for x in input().split()]
    if a[0] != 0:
        a = a[1:]
        for j in range(len(a)):
           x[i].children.append(x[a[j]-1])

for node in x:
    for child in node.children:
        child.is_root = False

for i in range(len(x)): 
    if x[i].is_root == True:
        print(i+1) 
    
