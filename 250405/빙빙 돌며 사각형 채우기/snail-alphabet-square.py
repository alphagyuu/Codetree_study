#print(ord("Z")-ord("A"))
#25
#print(chr(ord("A")+25))

N,M=map(int,input().split())
box=[
    ["0"]*M
    for _ in range(N)
]

def in_box(x,y):
    if x>=0 and y>=0 and x<M and y<N:
        return True
    else:
        return False

x=-1
y=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
d=0

i=0
while i<N*M:
    x_maybe=x+dx[d]
    y_maybe=y+dy[d]
    if in_box(x_maybe,y_maybe):
        if box[y_maybe][x_maybe]!="0":            
            d=(d+1)%4
        else:
            x=x_maybe
            y=y_maybe
            box[y][x]=chr(ord("A")+i%26)
            i+=1
    else:
        d=(d+1)%4
for row in box:
    print(*row)

### 14분
