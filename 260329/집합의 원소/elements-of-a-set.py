import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)  # 각 집합의 원소 개수 저장

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 경로 압축
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA != rootB:
        if size[rootA] < size[rootB]:
            parent[rootA] = rootB
            size[rootB] += size[rootA] # 사이즈 갱신
        else:
            parent[rootB] = rootA
            size[rootA] += size[rootB]

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        print(1 if find(a) == find(b) else 0)