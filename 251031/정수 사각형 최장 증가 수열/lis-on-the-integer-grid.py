n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
    
dp = [[1]*n for _ in range(n)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

points = []

for r in range(n):
    for c in range(n):
        points.append((grid[r][c],r,c))

points.sort()

def in_grid(r,c):
    return 0<=r<n and 0<=c<n

for x,r,c in points:
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if in_grid(nr,nc) and grid[nr][nc] > x:
            dp[nr][nc] = max(dp[nr][nc], dp[r][c]+1)

ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, dp[r][c])

print(ans)