N,M=map(int,input().split())

grid=[list(map(int,input().split())) for _ in range(N)]

top_col=dict()

drs=[1,0,-1,0]
dcs=[0,1,0,-1]

def in_grid(r,c):
    global N
    if 0<=r<N and 0<=c<N:
        return True
    return False

def explosion(C):
    global top_col,grid,N
    sr,sc=top_col.get(C,0),C
    for dr,dc in zip(drs,dcs):
        r,c=sr,sc
        for _ in range(grid[sr][sc]-1):
            r+=dr
            c+=dc
            if not in_grid(r,c):
                break
            elif grid[r][c]==0:
                continue
            else:
                grid[r][c]=0
                if top_col.get(c,0)==0:
                    top_col[c]=1
                else:
                    top_col[c]+=1
    grid[sr][sc]=0
    if top_col.get(sc,0)==0:
        top_col[sc]=1
    else:
        top_col[sc]+=1

def gravity(C,near):
    global grid,N,top_col
    for c in range(max(0,C-near),min(N,C+near)):
        temp=[]
        for r in range(N-1,-1,-1):
            if grid[r][c]==0:
                continue
            else:
                temp.append(grid[r][c])
        temp=temp+[0]*(N-len(temp))
        for r,t in zip(range(N-1,-1,-1),temp):
            grid[r][c]=t

for turn in range(M):
    C=int(input())
    C-=1
    if top_col.get(C,0)>=N:
        break
    near=grid[top_col.get(C,0)][C]
    explosion(C)
    gravity(C,near)

for row in grid:
    for n in row:
        print(n,end=" ")
    print("")