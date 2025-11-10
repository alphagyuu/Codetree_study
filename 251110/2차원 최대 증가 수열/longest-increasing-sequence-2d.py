N,M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

dp = [[1]*M for _ in range(N)]

ans = 0

for r in range(N):
    for c in range(M):
        for i in range(r+1,N):
            for j in range(c+1,M):
                if grid[i][j]>grid[r][c]:
                    dp[i][j] = max(dp[i][j], dp[r][c] + 1)
                    ans = max(ans,dp[i][j])
print(ans)