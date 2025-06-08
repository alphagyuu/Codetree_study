#배열로 다시풀기 (get() 메서드 시간복잡도 높음.)

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


for test_case in range(T):
    N,M=map(int,input().split())
    crashed=[False]*M
    balls.clear()
    ball_grid=[[0]*N for _ in range(N)]
    for i in range(M):
        r,c,d=map(str,input().split())
        r,c=int(r)-1,int(c)-1
        balls[i]=(r,c,d)
        ball_grid[r][c]+=1
    for turn in range(N*2+1):
        for i in range(M):
            if crashed[i]:
                continue
            r,c,d=balls[i]
            ball_grid[r][c]-=1
            nr,nc,nd=next(r,c,d)
            balls[i]=nr,nc,nd
            ball_grid[nr][nc]+=1
        temp=[]
        for i in range(M): 
            if crashed[i]:
                continue
            r,c,d=balls[i]
            if ball_grid[r][c]>1:
                crashed[i]=True
                temp.append((r,c))
        for tr,tc in temp:
            ball_grid[tr][tc]=0
    answer=M
    for i in range(M):
        if crashed[i]:
            answer-=1
    print(answer)