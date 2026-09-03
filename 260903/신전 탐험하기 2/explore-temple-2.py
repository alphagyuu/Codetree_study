n = int(input())

temple = []

# dp [층][방][시작방]
dp = [[[0]*3 for _ in range(3)] for _ in range(n)]

for _ in range(n):
    temple.append(list(map(int,input().split())))

for b in range(3):
    dp[0][b][b] = temple[0][b]

for i in range(1,n-1):
    for curb in range(3):
        for prevb in range(3):
            for startb in range(3):
                if curb != prevb:
                    dp[i][curb][startb] = max(dp[i][curb][startb], dp[i-1][prevb][startb] + temple[i][curb])

for curb in range(3):
    for prevb in range(3):
        for startb in range(3):
            if curb != prevb and curb != startb:
                dp[n-1][curb][startb] = max(dp[n-1][curb][startb], dp[n-2][prevb][startb] + temple[n-1][curb])

print(max(max(x) for x in dp[-1]))