N,M=map(int,input().split())
mgrid=[list(map(int,input().split())) for _ in range(N)]
Ms=tuple(map(int,input().split()))

grid=[[0]*N for _ in range(N)]
n2rci=dict()
for r in range(N):
    for c in range(N):
        n2rci[mgrid[r][c]]=(r,c,0)
        grid[r][c]=[mgrid[r][c]]

def in_grid(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

def nextrc(r,c):
    drs=[1,1,1,0,0,-1,-1,-1]
    dcs=[1,0,-1,1,-1,1,0,-1]
    maxn=0
    for dr,dc in zip(drs,dcs):
        nr,nc=r+dr,c+dc
        if not in_grid(nr,nc):
            continue
        nn=mgrid[nr][nc]
        if nn>maxn:
            maxn=nn
            ar,ac=nr,nc
    if maxn==0:
        return (-1,-1)
    else:
        return (ar,ac)

for m in Ms:
    r,c,idx=n2rci[m]
    nr,nc=nextrc(r,c)
    if nr==-1:
        continue
    nidx_start=len(grid[nr][nc])
    temp=grid[r][c][idx:]
    grid[r][c]=grid[r][c][:idx]
    grid[nr][nc]+=temp
    for i in range(len(temp)):
        n2rci[temp[i]]=(nr,nc,nidx_start+i)
    if len(grid[r][c])==0:
        mgrid[r][c]=0
    elif mgrid[r][c]==m:
        mgrid[r][c]=max(grid[r][c])
    #print(nr,nc,temp,mgrid,grid)

for row in grid:
    for ns in row:
        if len(ns)==0:
            print("None")
            continue
        ns.reverse()
        for n in ns:
            print(n,end=" ")
        print("")
