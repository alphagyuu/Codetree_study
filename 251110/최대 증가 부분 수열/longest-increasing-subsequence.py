N = int(input())

ns = list(map(int,input().split()))

dp = [1]*N

for i in range(N):
    for j in range(i+1,N):
        if ns[j]>ns[i]:
            dp[j] = max(dp[i]+1,dp[j])

print(max(dp))