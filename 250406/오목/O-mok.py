pan=[
    list(map(int,input().split()))
    for _ in range(19)
]

def check():
    before=pan[0][0]
    combo=0
    for i in range(19):
        for j in range(19):
            if pan[i][j] != 0:
                if before==pan[i][j]:
                    combo+=1
                else:
                    combo=1
                if combo==5:
                    return (before,i+1,j-1)
            before=pan[i][j]
    before=pan[0][0]
    combo=0
    for j in range(19):
        for i in range(19):
            if pan[i][j] != 0:
                if before==pan[i][j]:
                    combo+=1
                else:
                    combo=1
                if combo==5:
                    return (before,i-1,j+1)
            before=pan[i][j]
    before=pan[0][0]
    combo=0
    for i in range(0,15):
        x=i
        y=0
        while x<19:
            if pan[y][x]!=0:
                if before==pan[y][x]:
                    combo+=1
                else:
                    combo=1
                if combo==5:
                    return (before,x-1,y-1)
            before=pan[y][x]
            x+=1
            y+=1
    before=pan[1][0]
    combo=0    
    for i in range(1,15):
        x=0
        y=1
        while y<19:
            if pan[y][x]!=0:
                if before==pan[y][x]:
                    combo+=1
                else:
                    combo=1
                if combo==5:
                    return (before,x-1,y-1)
            before=pan[y][x]
            x+=1
            y+=1
    before=pan[0][4]
    combo=0
    for i in range(4,19):
        x=i
        y=0
        while x>=0:
            if pan[y][x]!=0:
                if before==pan[y][x]:
                    combo+=1
                else:
                    combo=1
                if combo==5:
                    return (before,y-1,x+3)
            before=pan[y][x]
            x-=1
            y+=1
    before=pan[18][1]
    combo=0                         
    for i in range(1,15):
        x=18
        y=i
        while y<19:
            if pan[y][x]!=0:
                if before==pan[y][x]:
                    combo+=1
                else:
                    combo=1
                if combo==5:
                    return (before,y-1,x+3)
            before=pan[y][x]
            x-=1
            y+=1    
    return -1
out=check()
if out==-1:
    print(-1)
else:
    print(out[0])
    print(*out[1:])        
        