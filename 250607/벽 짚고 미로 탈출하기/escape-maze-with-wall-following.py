N=int(input())
X,Y=map(int,input().split())
r=X-1
c=Y-1
grid=[[s for s in input()] for _ in range(N)]

drs=[0,1,0,-1]
dcs=[1,0,-1,0]

visited=[[False]*N for _ in range(N)]

def in_grid(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

def move(r,c,d,turn): #nr,nc,nd,turn 반환.
    if in_grid(r+drs[d],c+dcs[d]):
        if grid[r+drs[d]][c+dcs[d]]=="#":
            for i in range(-1,-4,-1):
                if not in_grid(r+drs[d+i],c+dcs[d+i]):
                    return r+drs[d+i],c+dcs[d+i],d+i,turn+1
                if grid[r+drs[d+i]][c+dcs[d+i]]==".":
                    nd=(d+i+4)%4
                    break
                if i==-3:
                    return r,c,d,-1
        else:
            nd=d            
    else:
        nd=d
    nr=r+drs[nd]
    nc=c+dcs[nd]
    if not in_grid(nr,nc):
        return nr,nc,nd,turn+1
    elif grid[nr+drs[(nd+1)%4]][nc+dcs[(nd+1)%4]]=="#":
        return nr,nc,nd,turn+1
    else:
        return nr+drs[(nd+1)%4],nc+dcs[(nd+1)%4],(nd+1)%4,turn+2

d,turn=0,0
while True:
    visited[r][c]=True
    r,c,d,turn=move(r,c,d,turn)
    if turn==-1:
        break
    if not in_grid(r,c):
        break
    if visited[r][c]:
        turn=-1
        break

#print(visited)
print(turn)