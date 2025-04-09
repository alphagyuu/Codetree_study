def is_exit(r,c):
    global N,M
    if r==N-1 and c==M-1:
        return True
    else:
        return False

def in_grid(r,c):
    global N,M
    if r>=0 and c>=0 and r<N and c<M:
        return True
    return False

CAN_EXIT=0

def dfs(r,c):
    global CAN_EXIT
    if CAN_EXIT==1:
        return
    if is_exit(r,c):
        CAN_EXIT = 1
        return
    dr=[1,0]
    dc=[0,1]
    for i in range(2):
        newr=r+dr[i]
        newc=c+dc[i]
        #새로운 값들이 격자를 벗어날 수 있음. -> 종료.
        if in_grid(newr,newc):
            if grid[newr][newc]==1:
                dfs(newr,newc)


N,M=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(N)
]

#뱀은 1로 표시된 visited 배열.
#visited=[[0]*M for _ in range(N)]
#for r in range(N):
#    for c in range(M):
#        visited[r][c]=grid[r][c]
#grid[N][M]
# N rows, M cols.
#print(grid)
#print(visited)
dfs(0,0)
print(CAN_EXIT)