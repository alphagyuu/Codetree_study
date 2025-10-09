from sortedcontainers import SortedSet

N,Q = map(int,input().split())

ns = list(map(int,input().split()))

s = SortedSet()

n2i=dict()

for i,n in enumerate(ns):
    s.add(n)
    n2i[n]=i

for _ in range(Q):
    a,b = map(int,input().split())
    bi=s.bisect_right(b)-1
    ai=max(s.bisect_left(a),0)-1 #자신보다 작은 값 중 가장 큰 인덱스
    print(bi-ai)