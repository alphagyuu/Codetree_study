N,M,R,C=map(int,input().split())
R-=1
C-=1


grid=[[False]*N for _ in range(N)]

drs=[1,0,-1,0]
dcs=[0,1,0,-1]

def in_grid(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

bombs=[(R,C)]
grid[R][C]=True

for t in range(M):
    distance=2**(t)
    temp=[]
    for r,c in bombs:
        for dr,dc in zip(drs,dcs):
            newr=r+dr*distance
            newc=c+dc*distance
            if in_grid(newr,newc) and not grid[newr][newc]:
                temp.append((newr,newc))
                grid[newr][newc]=True
    bombs+=temp

print(len(bombs))