n,m=map(int,input().split())

def next_pos(i,j,n,m):
    io=0
    jo=0
    if j==0 or i==(n-1): 
        io=0
        jo=j+i+1
        if jo>(m-1):
            io+=(jo-m+1)
            jo-=(jo-m+1)
    else:
        io=i+1
        jo=j-1
    return [io,jo]

arr=[
    [0 for i in range(m)]
    for j in range(n)
]

i=0
j=0
pos=[0,0]
for x in range(n*m):
    #print(i,j,x+1)
    arr[i][j]=x+1
    pos=next_pos(i,j,n,m)
    i=pos[0]
    j=pos[1]
for i in range(n):
    print(*arr[i])