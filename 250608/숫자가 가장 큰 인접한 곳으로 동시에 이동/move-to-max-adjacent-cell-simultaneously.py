N,M,T=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
balls=[]
for _ in range(M):
    r,c=map(int,input().split())
    r-=1
    c-=1
    balls.append((r,c))

crashed=[False]*M

def in_grid(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

def nextrc(r,c):
    drs=[-1,1,0,0]
    dcs=[0,0,-1,1]
    top=-1
    for dr,dc in zip(drs,dcs):
        nr,nc=r+dr,c+dc
        if in_grid(nr,nc):
            if grid[nr][nc]>top:
                top=grid[nr][nc]
                x,y=nr,nc
    return x,y

balls_dict=dict()
for t in range(T):
    balls_dict.clear()
    for i in range(M):
        if crashed[i]:
            continue
        r,c=balls[i]
        nr,nc=nextrc(r,c)
        balls[i]=(nr,nc)
        if balls_dict.get((nr,nc),0)>0:
            balls_dict[(nr,nc)]+=1
        else:
            balls_dict[(nr,nc)]=1
    for i in range(M):
        if crashed[i]:
            continue
        r,c=balls[i]
        if balls_dict[(r,c)]>1:
            crashed[i]=True

answer=0
for i in range(M):
    if not crashed[i]:
        answer+=1
print(answer)