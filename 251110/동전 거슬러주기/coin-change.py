N,M = map(int,input().split())

MAX = M*2

coins = list(map(int,input().split()))

coins.sort()

dp = [MAX]*(M+1)

for i in coins:
    if i>M:
        break
    dp[i] = 1

for i in range(coins[0]+1,M+1):
    min_path = MAX
    for c in coins:
        if (i-c)>0 and dp[i-c]<MAX:
            min_path = min(min_path, dp[i-c]+1)
    dp[i] = min(min_path,dp[i])

print(dp[-1] if dp[-1]<MAX else -1)