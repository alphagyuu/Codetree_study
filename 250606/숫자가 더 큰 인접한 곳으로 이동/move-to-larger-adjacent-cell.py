N,R,C=map(int,input().split())
R-=1
C-=1
grid=[list(map(int,input().split())) for _ in range(N)]

drs=[-1,1,0,0]
dcs=[0,0,-1,1]

def in_grid(r,c):
    global N
    if 0<=r<N and 0<=c<N:
        return True
    return False 

curr=R
curc=C
while True:
    nn=grid[curr][curc]
    print(nn,end=" ")
    can_move=False
    for dr,dc in zip(drs,dcs):
        if not in_grid(curr+dr,curc+dc):
            continue
        if grid[curr+dr][curc+dc]>nn:
            curr=curr+dr
            curc=curc+dc
            can_move=True
            break
    if not can_move:
        break
    