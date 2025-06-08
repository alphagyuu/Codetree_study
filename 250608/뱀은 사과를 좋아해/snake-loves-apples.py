from collections import deque

N,M,K=map(int,input().split())

grid=[[0]*N for _ in range(N)]

for _ in range(M):
    x,y=map(int,input().split())
    grid[x-1][y-1]="a"

def in_grid(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

#UDRL
drs=[-1,1,0,0]
dcs=[0,0,1,-1]
d2i={"U":0,"D":1,"R":2,"L":3}
r,c=0,0
grid[r][c]="s"
snake=deque()
snake.append((r,c))
TIME=0

done=False
for _ in range(K):
    d,p=map(str,input().split())
    p=int(p)
    for i in range(p):
        TIME+=1
        r+=drs[d2i[d]]
        c+=dcs[d2i[d]]
        if not in_grid(r,c):
            done=True
            break
        if grid[r][c]!="a":
            tr,tc=snake.popleft()
            grid[tr][tc]=0
        if grid[r][c]=="s":
            done=True
            break
        else:
            snake.append((r,c))
            grid[r][c]="s"
    if done:
        break

print(TIME)