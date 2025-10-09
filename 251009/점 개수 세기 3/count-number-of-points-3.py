N,Q = map(int,input().split())

ns = list(map(int,input().split()))

n2i=dict()

for i,n in enumerate(ns):
    n2i[n]=i

for _ in range(Q):
    a,b = map(int,input().split())
    bi=n2i[b]
    ai=n2i[a]
    print(bi-ai+1)