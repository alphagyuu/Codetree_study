N,M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*M for _ in range(N)]

dp[0][0] = 1

ans = 1

for r in range(N-1):
    for c in range(M-1):
        for i in range(r+1,N):
            for j in range(c+1,M):
                if grid[i][j]>grid[r][c]:
                    dp[i][j] = max(dp[i][j], dp[r][c] + 1)
                    ans = max(ans,dp[i][j])
print(ans)