from typing import List
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

def dfs(node: Node):
    node.is_visited = True
    for n in node.neighbor:
        if not n.is_visited:
            n.depth = node.depth+1
            dfs(n)

dfs(tree[0])
deepest = max(tree, key=lambda n:n.depth)
print(max([n.depth for n in tree]))
for node in tree:
    node.depth = 0
    node.is_visited = False

dfs(deepest)
print(max([n.depth for n in tree]))
