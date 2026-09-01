n, m = map(int,input().split())

coins = tuple(map(int,input().split()))

dp = [-1]*(m+1)

for c in coins:
    if c <= m:
        dp[c] = 1

for i in range(1,m+1):
    best = m*2
    for c in coins:
        if i-c > 0 and dp[i-c] > 0:
            best = min(best, dp[i-c])
    if best < m*2:
        if dp[i] > 0 :
            dp[i] = min(dp[i],best + 1)
        else:
            dp[i] = best + 1

print(dp[m])