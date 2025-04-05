N,M=map(int,input().split())
insts=[
    tuple(map(int,input().split()))
    for _ in range(M)
]

axis=[
    [0]*N
    for _ in range(N)
]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def in_axis(x,y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False

for x,y in insts:
    axis[y-1][x-1]=1
    cnt=0
    for i in range(4):
        x_c=x+dx[i]-1
        y_c=y+dy[i]-1
        if in_axis(x_c,y_c):
            cnt+=axis[y_c][x_c]
    print(1 if cnt>=3 else 0)
        
