T=int(input())
balls=dict()

def in_grid(r,c):
    global N
    if 0<=r<N and 0<=c<N:
        return True
    return False


def next(r,c,d):
    drs=[0,0,-1,1]
    dcs=[-1,1,0,0]
    d2i={"L":0,"R":1,"U":2,"D":3}
    rev={"L":"R","R":"L","U":"D","D":"U"}
    nr,nc=r+drs[d2i[d]],c+dcs[d2i[d]]
    if not in_grid(nr,nc):
        return r,c,rev[d]
    return nr,nc,d

rc_balls=dict()
for test_case in range(T):
    N,M=map(int,input().split())
    crashed=[False]*M
    balls.clear()
    for i in range(M):
        r,c,d=map(str,input().split())
        r,c=int(r)-1,int(c)-1
        balls[i]=(r,c,d)
    for turn in range(N*2+1):
        rc_balls.clear()
        for i in range(M):
            r,c,d=balls[i]
            nr,nc,nd=next(r,c,d)
            balls[i]=nr,nc,nd
            if crashed[i]:
                continue
            if rc_balls.get((nr,nc),0)>0:
                rc_balls[(nr,nc)]+=1
            else:
                rc_balls[(nr,nc)]=1
        for i in range(M):
            if crashed[i]:
                continue
            r,c,d=balls[i]
            if rc_balls[(r,c)]>1:
                crashed[i]=True
    answer=M
    for i in range(M):
        if crashed[i]:
            answer-=1
    print(answer)