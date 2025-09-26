import heapq

N,M,K=map(int,input().split())

ns=list(map(int,input().split()))

ms=list(map(int,input().split()))
ms.sort()

pq=[]

heapq.heapify(ns)

for _ in range(N):
    n=heapq.heappop(ns)
    for m in ms:
        heapq.heappush(pq,-(n+m))
        if len(pq)>K:
            heapq.heappop(pq)
        if (n+m)>(-pq[0]):
            break
    if n+ms[0]>(-pq[0]):
        break

print(-pq[0])