N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
n2rc=dict()
for r in range(N):
    for c in range(N):
        n2rc[grid[r][c]]=(r,c)

def in_grid(r,c):
    global N
    if 0<=r<N and 0<=c<N:
        return True
    return False 

def big_near_rc(r,c):
    drs=[1,0,-1,1,-1,1,0,-1]
    dcs=[-1,-1,-1,0,0,1,1,1]
    mn=-1
    for dr,dc in zip(drs,dcs):
        nr,nc=r+dr,c+dc
        if not in_grid(nr,nc):
            continue
        if grid[nr][nc]>mn:
            mr,mc=nr,nc
            mn=grid[nr][nc]
    return mr,mc


for turn in range(M):
    for n in range(1,N**2+1):
    #for n in range(1,2):
        r,c=n2rc[n]
        mr,mc=big_near_rc(r,c)
        grid[r][c],grid[mr][mc]=grid[mr][mc],grid[r][c]
        n2rc[n]=(mr,mc)
        n2rc[grid[r][c]]=(r,c)

for row in grid:
    for n in row:
        print(n,end=" ")
    print("")
