R,C=map(int,input().split())
grid=[
    list(map(str,input().split()))
    for _ in range(R)
]

cnt=0
def next(grid,x,y,turn):
    global cnt
    c=grid[y][x]
    #print(x,y,turn,c)
    if turn==3:
        if (x,y)==(C-1,R-1):
            cnt+=1
        return
    if x<C and y<R:
        for j in range(x+1,C):
            for i in range(y+1,R):
                if grid[i][j]!=c:
                    next(grid,j,i,turn+1)

next(grid,0,0,0)
print(cnt)
