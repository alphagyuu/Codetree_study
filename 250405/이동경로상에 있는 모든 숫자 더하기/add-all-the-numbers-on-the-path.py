N,T=map(int,input().split())
insts=list(input())
box=[
    list(map(int,input().split()))
    for _ in range(N)
]


dx=[0,1,0,-1]
dy=[-1,0,1,0]
d=0
x=N//2
y=N//2

def in_box(x,y):
    if x>=0 and x<N and y>=0 and y<N:
        return(True)
    else:
        return(False)
tot=box[y][x]
for i in insts:
    if i=="R":
        d=(d+1)%4
    elif i=="L":
        d=(d-1)%4
    else:
        if in_box(x+dx[d],y+dy[d]):
            x+=dx[d]
            y+=dy[d]
            tot+=box[y][x]
    #print(x,y)
print(tot)


#20분