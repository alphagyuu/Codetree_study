from heapq import heappush, heappop

MAX_INT = 100

N, M = map(int,input().split())

K = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,d = map(int,input().split())
    graph[s].append((d,e))
    graph[e].append((d,s))

dist = [MAX_INT]*(N+1)

def dijkstra(K):
    global dist
    pq = []
    dist[K] = 0
    heappush(pq,(0,K))
    while pq:
        min_d, min_i = heappop(pq)

        if min_d > dist[min_i]:
            continue

        for d, i in graph[min_i]:
            new_d = dist[min_i] + d
            if new_d < dist[i]:
                dist[i] = new_d
                heappush(pq, (new_d, i))

dijkstra(K)

for i in range(1,N+1):
    print(dist[i])