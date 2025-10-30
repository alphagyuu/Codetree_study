N=int(input())

grid=[list(map(int,input().split())) for _ in range(N)]

hap=[[0]*N for _ in range(N)]

hap[0][0] = grid[0][0]
for i in range(1,N):
    hap[0][i] = hap[0][i-1] + grid[0][i]
    hap[i][0] = hap[i-1][0] + grid[i][0]

for i in range(1,N):
    for j in range(1,N):
        hap[i][j] = grid[i][j] + max(hap[i][j-1], hap[i-1][j])

print(hap[-1][-1])