n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)  # 각 집합의 원소 개수 저장

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 경로 압축
    return parent[x]

def union(a,b):
    roota = find(a)
    rootb = find(b)
    if roota != rootb:
        if size[roota] < size[rootb]:
            parent[roota] = rootb
            size[rootb] += size[roota]
        else:
            parent[rootb] = roota
            size[roota] += size[rootb]

for _ in range(m):
    type,a,b = map(int,input().split())
    if type == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)