import heapq

N,M,K=map(int,input().split())

ns=list(map(int,input().split()))

ms=list(map(int,input().split()))

pq=[]

for n in ns:
    for m in ms:
        heapq.heappush(pq,(n+m,n,m))

for _ in range(K-1):
    heapq.heappop(pq)

print(pq[0][0])