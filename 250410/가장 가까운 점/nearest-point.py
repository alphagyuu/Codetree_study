import heapq

N,M=map(int,input().split())

dots=[]
for _ in range(N):
    x,y=map(int,input().split())
    heapq.heappush(dots,(x+y,(x,y)))

for _ in range(M):
    _,(x,y)=heapq.heappop(dots)
    heapq.heappush(dots,(x+y+4,(x+2,y+2)))

_,(x,y)=heapq.heappop(dots)
print(x,y)