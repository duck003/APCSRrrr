from typing import List
from collections import deque
N = int(input())

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbor: List[Node] = []
        self.is_visited = False
        self.is_root = True
        self.depth = 0

tree: List[Node] = [Node(i) for i in range(N)]

for _ in range(N-1):
    i,j = map(int, input().split())
    tree[i].neighbor.append(tree[j])
    tree[j].neighbor.append(tree[i])

def bfs(root: Node):
    q = deque([root])
    while q:
        front = q.popleft() 
        front.is_visited = True
        for n in front.neighbor:
            if not n.is_visited:
                front.depth = front.depth + 1
                q.append(n)
            
bfs(tree[0])
deepest = max(tree, key=lambda n:n.depth)

for node in tree:
    node.depth = 0
    node.is_visited = False

bfs(deepest)
print(max([n.depth for n in tree]))
