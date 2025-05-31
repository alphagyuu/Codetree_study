import heapq
N=int(input())
heap=[]
for turn in range(N):
    n=int(input())
    if n==0:
        if len(heap)==0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,-n)
