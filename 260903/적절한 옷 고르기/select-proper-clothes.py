from collections import defaultdict
n,m = map(int,input().split())

clothes = [[] for _ in range(m)]
dp = [defaultdict(int) for _ in range(m)]

for _ in range(n):
    s,e,v = map(int,input().split())
    for day in range(s-1,e):
        clothes[day].append(v)

for c in clothes[0]:
    dp[0][c] = 0
for i in range(1,m):
    for tc in clothes[i]:
        for yc in dp[i-1]:
            dp[i][tc] = max(dp[i][tc],dp[i-1][yc]+abs(tc-yc))


candidates = [dp[-1][x] for x in dp[-1]]

print(max(candidates))