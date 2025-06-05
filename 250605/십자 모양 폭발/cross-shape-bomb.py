N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]

r,c=map(int,input().split())
r-=1
c-=1

def in_grid(r,c):
    global N
    if 0<=r<N and 0<=c<N:
        return True
    return False

drs=[1,0,-1,0]
dcs=[0,1,0,-1]


for dr,dc in zip(drs,dcs):
    curr=r
    curc=c
    for i in range(grid[r][c]-1):
        curr+=dr
        curc+=dc
        if in_grid(curr,curc):
            grid[curr][curc]=0
        else:
            break
grid[r][c]=0

for c in range(N):
    temp=[]
    zeros=0
    for r in range(N-1,-1,-1):
        n=grid[r][c]
        if n==0:
            zeros+=1
        else:
            temp.append(n)
    temp+=[0]*zeros
    for r in range(N):
        grid[r][c]=temp[N-1-r]

for row in grid:
    for n in row:
        print(n,end=" ")
    print("")