import heapq

N,M,K=map(int,input().split())

ns=list(map(int,input().split()))

ms=list(map(int,input().split()))

pq=[]

for n in ns:
    for m in ms:
        heapq.heappush(pq,-(n+m))
        if len(pq)>K:
            heapq.heappop(pq)

print(-pq[0])