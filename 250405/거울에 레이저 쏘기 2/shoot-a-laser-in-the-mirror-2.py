#이동
#if 바깥 -> 종료
#if /\,이전 방향 합쳐서 방향변경

N=int(input())
grid=[
    list(input())
    for _ in range(N)
]
#print(grid)
K=int(input())

K-=1
if K//N==0:
    y=-1
    x=K
    d=0
elif K//N==1:
    x=N
    y=(K%N)
    d=1
elif K//N==2:
    x=N-1-(K%N)
    y=N
    d=2
else:
    x=-1
    y=N-1-(K%N)
    d=3
#print(x,y)

def out(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return True
    else: 
        return False

dx=[0,-1,0,1]
dy=[1,0,-1,0]
#D L U R

cnt=0
while True:
    x+=dx[d]
    y+=dy[d]
    if out(x,y):
        break
    else:
        if grid[y][x]=="/":
            if d%2==0:
                d+=1
            else:
                d-=1
        else:
            if d%2==0:
                d=(d-1)%4
            else:
                d=(d+1)%4
        cnt+=1
    #print(x,y,d)
print(cnt)