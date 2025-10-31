n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
hap = [[0]*n for _ in range(n)]

hap[0][n-1] = grid[0][n-1]

for i in range(n-2,-1,-1):
    hap[0][i] = grid[0][i] + hap[0][i+1]
for i in range(1,n):
    hap[i][n-1] = grid[i][n-1] + hap[i-1][n-1]

for r in range(1,n):
    for c in range(n-2,-1,-1):
        hap[r][c] = grid[r][c] + min(hap[r-1][c],hap[r][c+1])

print(hap[n-1][0])