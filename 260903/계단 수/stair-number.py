n = int(input())

dp = [[0]*10 for _ in range(n)]
for x in range(1,10):
    dp[0][x] = 1

for i in range(1,n):
    for x in range(1,9):
        dp[i][x] = dp[i-1][x-1] + dp[i-1][x+1]
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

print(sum(dp[-1])%(10**9+7))