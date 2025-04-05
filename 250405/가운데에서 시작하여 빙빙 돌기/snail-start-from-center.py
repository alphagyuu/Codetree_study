N=int(input())
box=[
    [0]*N
    for _ in range(N)
]
x=N//2
y=N//2
#print(x,y)
dx=[1,0,-1,0]
dy=[0,-1,0,1]
d=3
def in_box(x,y):
    if x>=0 and y>=0 and x<N and y<N:
        return True
    else:
        return False

for i in range(N*N):
    box[y][x]=i+1
    if box[y+dy[(d+1)%4]][x+dx[(d+1)%4]]==0:
        d=(d+1)%4
    x=x+dx[d]
    y=y+dy[d]
for row in box:
    print(*row)


        