from collections import deque

drs=[-1,-2,-2,-1,1,2,2,1]
dcs=[-2,-1,1,2,2,1,-1,-2]

def in_grid(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

def bfs(r,c):
    queue=deque()
    visited[r][c]=True
    distance_matrix[r][c]=0
    queue.append((r,c))
    while queue:
        curr,curc=queue.popleft()
        for d in range(8):
            newr=curr+drs[d]
            newc=curc+dcs[d]
            if in_grid(newr,newc) and not visited[newr][newc]:
                visited[newr][newc]=True
                distance_matrix[newr][newc]=distance_matrix[curr][curc]+1
                queue.append((newr,newc))



N=int(input())
r1,c1,r2,c2=map(int,input().split())
#print(r1,c1,r2,c2)
visited=[[False]*N for _ in range(N)]
distance_matrix=[[-1]*N for _ in range(N)]
#BFS: 방문할수 있는 모든 지점에 "최단시간"을 기록할 수 있음.
bfs(r1-1,c1-1)
print(distance_matrix[r2-1][c2-1])
