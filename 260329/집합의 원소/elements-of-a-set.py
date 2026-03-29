n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

for _ in range(m):
    c, a, b = map(int,input().split())
    if c == 0:
        parent[b] = a
    else:
        print(1 if find(a) == find(b) else 0)