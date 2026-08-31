import heapq
from collections import defaultdict
N = int(input())

def bfs():
    q = []
    heapq.heappush(q,(0,N))
    visited = defaultdict(bool)
    visited[N] = True
    while q:
        turn,x = heapq.heappop(q)
        if x == 1:
            print(turn)
            return
        if not visited[x+1]:
            heapq.heappush(q,(turn+1,x+1))
            visited[x+1] = True
        if not visited[x-1]:
            heapq.heappush(q,(turn+1,x-1))
            visited[x-1] = True
        if x%2 == 0 and not visited[x//2]:
            heapq.heappush(q,(turn+1,x//2))
            visited[x//2] = True
        if x%3 == 0 and not visited[x//3]:
            heapq.heappush(q,(turn+1,x//3))
            visited[x//3] = True

bfs()