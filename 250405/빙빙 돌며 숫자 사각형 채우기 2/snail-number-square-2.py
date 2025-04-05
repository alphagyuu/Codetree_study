#일단 채워. -> 가려고 해 -> 불가능이면 방향만 바꿔(i증가x) 반복. XXXX
# -1에서 출발
N,M=map(int,input().split())
box=[
    [0]*M
    for _ in range(N)
]

def in_box(x,y):
    if x>=0 and y>=0 and x<M and y<N:
        return True
    else:
        return False
dx=[0,1,0,-1]
dy=[1,0,-1,0]
i=0
x=0
y=-1
d=0

while i<N*M:
    x_maybe=x+dx[d]
    y_maybe=y+dy[d]
    if in_box(x_maybe,y_maybe):
        if box[y_maybe][x_maybe]!=0:
            d=(d+1)%4
        else:
            x=x_maybe
            y=y_maybe
            i+=1
            box[y][x]=i
    else:
        d=(d+1)%4
    
for row in box:
    print(*row)
    

### 11분 13초