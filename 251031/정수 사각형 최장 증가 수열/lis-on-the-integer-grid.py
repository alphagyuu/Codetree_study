from collections import deque

n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]
    
dp = [[1]*n for _ in range(n)]

def in_grid(r,c):
    return 0<=r<n and 0<=c<n

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs(r,c):
    q = deque()
    q.append((r,c,1))
    while q:
        cr,cc,cm = q.popleft()
        nm = cm + 1
        for d in range(4):
            nr,nc = cr+dr[d], cc+dc[d]
            if in_grid(nr,nc) and grid[nr][nc] > grid[cr][cc] and dp[nr][nc] < nm:
                dp[nr][nc] = nm
                q.append((nr,nc,nm))

for r in range(n):
    for c in range(n):
        if dp[r][c] == 1:
            bfs(r,c)

ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans,dp[r][c])

print(ans)