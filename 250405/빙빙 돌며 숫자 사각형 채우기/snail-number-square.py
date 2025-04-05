N,M=map(int,input().split())
box=[
    [0]*M
    for _ in range(N)
]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

x=0
y=0
d=0
x_maybe=0
y_maybe=0
def in_box(x,y):
    if x>=0 and x<M and y>=0 and y<N:
        return True
    else:
        return False
for i in range(N*M):
    box[y][x]=i+1
    x_maybe=x+dx[d]
    y_maybe=y+dy[d]
    if in_box(x_maybe,y_maybe):
        if box[y_maybe][x_maybe]>0:
            d=(d+1)%4
    else:
        d=(d+1)%4
    x+=dx[d]
    y+=dy[d]
for row in box:
    print(*row)

    
