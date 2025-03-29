n,m=map(int,input().split())

i=0
j=0
def next_move(i,j):
    im=0
    jm=0
    if(i==0 and j%2==1):
        jm=1
    elif(i==(n-1) and j%2==0):
        jm=1
    elif(j%2==0):
        im=1
    else:
        im=-1
    return [im,jm]
arr=[
    [0 for i in range(m)]
    for _ in range(n)
]
move=[0,0]
for x in range(n*m):
    arr[i][j]=x
    move=next_move(i,j)
    i+=move[0]
    j+=move[1]
for i in range(n):
    print(*arr[i])
    