def can_go(r,c,val):
    if r>=0 and c>=0 and r<N and c<N:
        if grid[r][c]==val and visited[r][c]==0:
            return True
    return False

def dfs(r,c):
    visited[r][c]=1
    global BLOCK_SIZE
    global val
    BLOCK_SIZE+=1
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]
    for i in range(4):
        newr=r+dr[i]
        newc=c+dc[i]
        if can_go(newr,newc,val):
            dfs(newr,newc)


N=int(input())
grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
# row, col: N
visited=[
    [0]*N
    for _ in range(N)
]

MAX_BLOCK_SIZE=0
TOTAL_POP=0
for r in range(N):
    for c in range(N):
        if visited[r][c]==0:
            val=grid[r][c]
            BLOCK_SIZE=0
            dfs(r,c)
            if BLOCK_SIZE>=4:
                TOTAL_POP+=1
            if BLOCK_SIZE>MAX_BLOCK_SIZE:
                MAX_BLOCK_SIZE=BLOCK_SIZE
print(TOTAL_POP,MAX_BLOCK_SIZE)

