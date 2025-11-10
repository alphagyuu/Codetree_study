MAX = 10001

N, M = map(int,input().split())

A = list(map(int,input().split()))

dp = [MAX]*(M+1)

for i in range(N):
    if A[i]>M:
        continue
    for j in range(M-A[i],-1,-1):
        if dp[j]<MAX:
            dp[A[i]+j] = min(dp[A[i]+j],dp[j]+1)
    dp[A[i]] = 1
    
print(dp[M] if dp[M] < MAX else -1)