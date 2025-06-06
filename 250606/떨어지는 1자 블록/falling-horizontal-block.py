N,M,K=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]

def tetris():
    global N,M,K
    for r in range(1,N):
        for c in range(K-1,M+K-1):
            if grid[r][c]==1:
                for c in range(K-1,M+K-1):
                    grid[r-1][c]=1
                return
    for c in range(K-1,M+K-1):
        grid[N-1][c]=1

tetris()

for row in grid:
    for n in row:
        print(n,end=" ")
    print("")