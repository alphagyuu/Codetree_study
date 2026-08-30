from collections import deque

N, M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def in_grid(r,c):
    return 0<=r<N and 0<=c<M

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        r, c = q.pop()
        if (r,c) == (N-1,M-1):
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if in_grid(nr,nc) and grid[nr][nc] == 1 and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = True
    return 0

print(bfs())