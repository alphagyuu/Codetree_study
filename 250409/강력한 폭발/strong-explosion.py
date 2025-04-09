def in_grid(r,c):
    if r>=0 and c>=0 and r<N and c<N:
        return True
    else:
        return False
dr1=[-2,-1,0,1,2]

dr2=[-1,0,1,0,0]
dc2=[0,1,0,-1,0]

dr3=[-1,-1,1,1,0]
dc3=[-1,1,1,-1,0]

#폭발 3가지를 모두 simulate.
def explosion(r,c,type):
    if type==1:
        for i in range(5):
            rcur=r+dr1[i]
            ccur=c
            if in_grid(rcur,ccur):
                grid_exploded[rcur][ccur]=1
    elif type==2:
        for i in range(5):
            rcur=r+dr2[i]
            ccur=c+dc2[i]
            if in_grid(rcur,ccur):
                grid_exploded[rcur][ccur]=1
    elif type==3:
        for i in range(5):
            rcur=r+dr3[i]
            ccur=c+dc3[i]
            if in_grid(rcur,ccur):
                grid_exploded[rcur][ccur]=1
    return

MAX_AREA=0

def simulate(BOMB_TYPES):
    global grid_exploded
    global MAX_AREA
    grid_exploded = [[0]*N for _ in range(N)]
    for i in range(BOMB_NUM):
        rsim,csim=BOMB_RCS[i]
        explosion(rsim,csim,BOMB_TYPES[i])
    exploded_area=0
    for row in grid_exploded:
        exploded_area+=row.count(1)
    if MAX_AREA<exploded_area:
        MAX_AREA=exploded_area
    return exploded_area



BOMB_TYPES=[]
# 백트레킹
def iterate(cur):
    if cur==BOMB_NUM:
        simulate(BOMB_TYPES)
        return
    for t in range(1,4):
        BOMB_TYPES.append(t)
        iterate(cur+1)
        BOMB_TYPES.pop()

N=int(input())
BOMB_NUM = 0 # 폭탄 개수
BOMB_RCS=[] # 폭탄 좌표
grid_bomb=[list(map(int,input().split())) for _ in range(N)]
grid_exploded = [[0] * N for _ in range(N)]
#print(grid_bomb)

for r in range(N):
    for c in range(N):
        if grid_bomb[r][c]==1:
            BOMB_RCS.append((r,c))
            BOMB_NUM+=1
MAX_AREA = 0
iterate(0)
print(MAX_AREA)

'''
    print(BOMB_NUM)
    print(BOMB_RCS)
    grid_exploded = [[0]*N for _ in range(N)]
    print(grid_exploded)
    explosion(1,1,3)
    print(grid_exploded)
'''