n = int(input())
sequences = [input() for _ in range(n)]

class node:
    def __init__(self):
        self.is_end = False
        self.children = dict()

nodes = dict()

nodes[""] = node()

prefix_yes = 1

for seq in sequences:
    if seq in nodes: 
        if not nodes[seq].is_end:
            prefix_yes = 0
    cur = ""
    for c in seq:
        if cur+c not in nodes[cur].children:
            nodes[cur+c] = node()
            nodes[cur].children[cur+c] = nodes[cur+c]
        elif nodes[cur+c].is_end:
            prefix_yes = 0
        cur+=c
    nodes[cur].is_end = True

print(prefix_yes)
    
        