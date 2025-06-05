grid=[list(map(int,input().split())) for _ in range(4)]
DIR=input()


if DIR=="L":
    for r in range(4):
        grav=[]
        for c in range(4):
            if grid[r][c]!=0:
                grav.append(grid[r][c])
        grav=grav+[0]*(4-len(grav))
        for c in range(4):
            grid[r][c]=grav[c]
        temp=[]
        used=[False]*5
        for c in range(4):
            if used[c] or grid[r][c]==0:
                continue
            if c==3:
                temp.append(grid[r][c])
            elif grid[r][c+1]==grid[r][c]:
                used[c]=True
                used[c+1]=True
                temp.append(grid[r][c]*2)
            else:
                temp.append(grid[r][c])
        temp=temp+[0]*(4-len(temp))
        for c,t in zip(range(4),temp):
            grid[r][c]=t

if DIR=="R":
    for r in range(4):
        grav=[]
        for c in range(3,-1,-1):
            if grid[r][c]!=0:
                grav.append(grid[r][c])
        grav=grav+[0]*(4-len(grav))
        for c in range(3,-1,-1):
            grid[r][c]=grav[3-c]
        temp=[]
        used=[False]*5
        for c in range(3,-1,-1):
            if used[c] or grid[r][c]==0:
                continue
            if c==0:
                temp.append(grid[r][c])
            elif grid[r][c-1]==grid[r][c]:
                used[c]=True
                used[c-1]=True
                temp.append(grid[r][c]*2)
            else:
                temp.append(grid[r][c])
        temp=temp+[0]*(4-len(temp))
        for c,t in zip(range(3,-1,-1),temp):
            grid[r][c]=t

if DIR=="U":
    for c in range(4):
        grav=[]
        temp=[]
        used=[False]*5
        for r in range(4):
            if grid[r][c]!=0:
                grav.append(grid[r][c])
        grav=grav+[0]*(4-len(grav))
        for r in range(4):
            grid[r][c]=grav[r]
        for r in range(4):
            if used[r] or grid[r][c]==0:
                continue
            if r==3:
                temp.append(grid[r][c])
            elif grid[r+1][c]==grid[r][c]:
                used[r]=True
                used[r+1]=True
                temp.append(grid[r][c]*2)
            else:
                temp.append(grid[r][c])
        temp=temp+[0]*(4-len(temp))
        for r,t in zip(range(4),temp):
            grid[r][c]=t

if DIR=="D":
    for c in range(4):
        grav=[]
        for r in range(3,-1,-1):
            if grid[r][c]!=0:
                grav.append(grid[r][c])
        grav=grav+[0]*(4-len(grav))
        for r in range(3,-1,-1):
            grid[r][c]=grav[3-r]
        temp=[]
        used=[False]*5
        for r in range(3,-1,-1):
            if used[r] or grid[r][c]==0:
                continue
            if r==0:
                temp.append(grid[r][c])
            elif grid[r-1][c]==grid[r][c]:
                used[r]=True
                used[r-1]=True
                temp.append(grid[r][c]*2)
            else:
                temp.append(grid[r][c])
        temp=temp+[0]*(4-len(temp))
        for r,t in zip(range(3,-1,-1),temp):
            grid[r][c]=t

for row in grid:
    for n in row:
        print(n,end=" ")
    print("")