from heapq import heappush, heappop

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
dist = [10000]*(N+1)

for _ in range(M):
    i, j, d = map(int,input().split())
    graph[j].append((d,i))

pq = []
heappush(pq, (0,N))
dist[N] = 0

while pq:
    min_d, min_i = heappop(pq)
    if dist[min_i] != min_d:
        continue
    for d, i in graph[min_i]:
        if min_d + d < dist[i]:
            dist[i] = min_d + d
            heappush(pq,(dist[i], i))

print(max(dist[1:]))