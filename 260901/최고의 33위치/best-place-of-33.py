n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

def cnt(r,c):
    ans = 0
    for i in range(r,min(r+3,n)):
        for j in range(c,min(c+3,n)):
            if grid[i][j] == 1:
                ans += 1
    return ans

ans = 0
for r in range(n-2):
    for c in range(n-2):
       ans = max(ans,cnt(r,c))

print(ans) 