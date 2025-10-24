from itertools import combinations
from collections import deque

N, K, M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

drs = [1,-1,0,0]
dcs = [0,0,1,-1]

def in_grid(r,c):
    return 0<=r<N and 0<=c<N

ri = 0
rocks = dict()
xy2ri = dict()
for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            xy2ri[(r,c)] = ri
            rocks[ri] = (r,c)
            ri+=1

def BFS(r,c,removed_rocks):
    q = deque()
    visited[r][c] = True
    q.append((r,c))
    cnt = 1
    while q:
        cr,cc = q.popleft()
        for d in range(4):
            nr,nc = cr + drs[d], cc+ dcs[d]
            if not in_grid(nr,nc):
                continue
            if not visited[nr][nc]:
                if grid[nr][nc] == 1:
                    if xy2ri[(nr,nc)] not in removed_rocks:
                        continue
                visited[nr][nc] = True
                cnt +=1
                q.append((nr,nc))

max_cnt = 0
riter = [i for i in range(len(rocks))]

starts = []
for _ in range(K):
    r,c = map(int,input().split())
    starts.append((r,c))

for rocks in list(combinations(riter,M)):
    visited = [ [False]*N for _ in range(N) ]
    for r,c in starts:
        BFS(r-1,c-1,rocks)
    cnt = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                cnt+=1
    max_cnt = max(max_cnt,cnt)

print(max_cnt)