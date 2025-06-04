N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
R,C,M1,M2,M3,M4,DIR=map(int,input().split())

R=R-1
C=C-1

drs=[[-1,-1,1,1],[-1,-1,1,1]]
dcs=[[-1,1,1,-1],[1,-1,-1,1]]

def nextrc(r,c,DIR,turn):
    global M1,M2,M3,M4
    go=0
    if DIR==0:
        if turn<M4:
            go=0
        elif turn<M4+M3:
            go=1
        elif turn<M4+M3+M2:
            go=2
        else:
            go=3
    else:
        if turn<M1:
            go=0
        elif turn<M1+M2:
            go=1
        elif turn<M1+M2+M3:
            go=2
        else:
            go=3
    return r+drs[DIR][go],c+dcs[DIR][go]

r,c=R,C
first=grid[r][c]
for turn in range(M1+M2+M3+M4-1):
    nr,nc=nextrc(r,c,DIR,turn)
    grid[r][c]=grid[nr][nc]
    r,c=nr,nc
nr,nc=nextrc(r,c,DIR,turn)
grid[r][c]=first

for row in grid:
    for v in row:
        print(v,end=" ")
    print("")
    