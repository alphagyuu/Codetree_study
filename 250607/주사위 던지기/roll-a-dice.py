N,M,r,c=map(int,input().split())
r-=1
c-=1
moves=tuple(map(str,input().split()))
grid=[[0]*N for _ in range(N)]

dice=[
    [[6,3,1,4],[2,5]], #BRTL DU
    [[6,2,1,5],[3,4]] #BDTU RL
]

def roll(d):
    if d=="L":
        dice[0][0]=[dice[0][0][-1]]+dice[0][0][0:3]
        dice[1][0]=[dice[0][0][0],dice[0][1][0],dice[0][0][2],dice[0][1][1]]
        dice[1][1]=[dice[0][0][1],dice[0][0][3]]
    elif d=="R":
        dice[0][0]=dice[0][0][1:]+[dice[0][0][0]]
        dice[1][0]=[dice[0][0][0],dice[0][1][0],dice[0][0][2],dice[0][1][1]]
        dice[1][1]=[dice[0][0][1],dice[0][0][3]]
    elif d=="U":
        dice[1][0]=[dice[1][0][-1]]+dice[1][0][0:3]
        dice[0][0]=[dice[1][0][0],dice[1][1][0],dice[1][0][2],dice[1][1][1]]
        dice[0][1]=[dice[1][0][1],dice[1][0][3]]
    else:
        dice[1][0]=dice[1][0][1:]+[dice[1][0][0]]
        dice[0][0]=[dice[1][0][0],dice[1][1][0],dice[1][0][2],dice[1][1][1]]
        dice[0][1]=[dice[1][0][1],dice[1][0][3]]


#LRUD
drs=[0,0,-1,1]
dcs=[-1,1,0,0]
m2d={"L":0,"R":1,"U":2,"D":3}

def in_grid(r,c):
    global N
    if 0<=r<N and 0<=c<N:
        return True
    return False

grid[r][c]=6
for d in moves:
    nextr=r+drs[m2d[d]]
    nextc=c+dcs[m2d[d]]
    if in_grid(nextr,nextc):
        r,c=nextr,nextc
        roll(d)
        grid[r][c]=dice[0][0][0]

answer=0
for r in range(N):
    for c in range(N):
        answer+=grid[r][c]

print(answer)