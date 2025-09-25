import heapq

N, M = map(int,input().split())

ns=list(map(int,input().split()))

pq=[]

for n in ns:
    heapq.heappush(pq,-n)

for _ in range(M):
    n=-heapq.heappop(pq)
    heapq.heappush(pq,-(n-1))

print(-pq[0])