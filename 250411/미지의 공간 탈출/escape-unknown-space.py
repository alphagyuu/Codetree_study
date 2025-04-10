# 4/10 23:40
# 4/11 03:40
from collections import deque


drs=[0,0,1,-1]
dcs=[1,-1,0,0]
#동 서 남 북

#연속적인 단일 bfs함수에서 구현.
#wall_grid에서 다른 공간으로의 이동:
#dx,dy 테크닉을 사용하고 나서 경계를 벗어나면:
#공간이동. ( 현재 공간을 변수로 관리하자. NOW_MAP)
#거리값은 연속해서 저장.

def print_grid(x):
    for g in x:
        for row in g:
            print(*row)
        print("")

def in_grid(r,c,now_map):
    if r>=0 and c>=0:
        if now_map<5:
            if r<M and c<M:
                return True
        else:
            if r<N and c<N:
                return True
    return False


# 벗어난 경우:  ##반드시 일단 이동 후에 적용해야 함.
# 커넥션 밟은경우 - 반대 커넥션으로 이동.
# 현재 맵에 따라
#
# 5에서는 맵 외부 이동 X.
def map_move(r,c,now_map):
    global N, M, connection_wall, connection_miji
    if (r-1,c,now_map) == connection_wall:
        return connection_miji

    if in_grid(r,c,now_map):
        return (r,c,now_map)
    else: #맵을 벗어난 경우. (이동조건이 아니면 벗어난좌표 그대로 반환.
        if now_map==5:
            return (r,c,now_map)

        #위에서
        elif now_map==4:
            if c>M-1: #오른쪽
                return (0,M-1-r,0)
            if c<0: #왼쪽
                return (0,r,1)
            if r>M-1: #아래
                return (0,c,2)
            if r<0:
                return (0,M-1-c,3)

        else:
            left_map=[2,3,1,0]
            right_map=[3,2,0,1]
            if c > M - 1:  # 오른쪽
                return(r,0,right_map[now_map])
            if c < 0:  # 왼쪽
                return(r,M-1,left_map[now_map])
            if r<0: # 위
                if now_map==0:
                    return(M-1-c,M-1,4)
                if now_map==1:
                    return(c,0,4)
                if now_map==2:
                    return(M-1,c,4)
                if now_map==3:
                    return(0,M-1-c,4)
            else:
                return(r,c,now_map)
    return (r,c,now_map)




def event_process(T):
    global F
    if T==0:
        return
    if T-1 not in turn_events:
        event_process(T-1)
    if T in turn_events:
        return
    temp=[]
    for i in range(len(strange_event)):
        r,c,d,v=strange_event[i]
        if T==0:
            grid[5][r][c]=7
        elif T%v==0:
            newr=r+drs[d]
            newc=c+dcs[d]
            if in_grid(newr,newc,5):
                if grid[5][newr][newc]==0:
                    grid[5][newr][newc]=7
                    strange_event[i][0]=newr
                    strange_event[i][1]=newc
                    temp.append((newr,newc,5))
    turn_events[T]=turn_events[T-1]+temp
    return

def find_start():
    for r in range(M):
        for c in range(M):
            if wall_grid[4][r][c]==2:
                return (r,c,4)

#wall_grid[4]의 2지점에서 출발.
def bfs(r,c,now_map):
    if not in_grid(r,c,now_map):
        print(-1)
        return
    queue=deque()
    visited[now_map][r][c]=True
    distance[now_map][r][c]=0
    queue.append((r,c,now_map))

    while queue: # 턴을 확실하게 관리하자.
        curr,curc,cur_map=queue.popleft()
        for d in range(4):
            newr, newc, new_map=map_move(curr+drs[d],curc+dcs[d],cur_map)
            #print(newr,newc,new_map)
            if in_grid(newr,newc,new_map):
                next_turn=distance[cur_map][curr][curc]+1
                if next_turn not in turn_events:
                    event_process(next_turn)
                if grid[new_map][newr][newc]==0 and ((newr,newc,new_map) not in turn_events[next_turn]):
                    if visited[new_map][newr][newc]==False:
                        visited[new_map][newr][newc]=True
                        distance[new_map][newr][newc]=distance[cur_map][curr][curc]+1
                        queue.append((newr,newc,new_map))
                if grid[new_map][newr][newc]==4:
                    global ANSWER
                    ANSWER=next_turn
                    return



def find_3_in_miji():
    global N,M
    first3_in_miji = True
    for r in range(N):
        for c in range(N):
            if miji_grid[r][c] == 3:
                if first3_in_miji:
                    r3_0, c3_0 = r, c
                    first3_in_miji = False
                    return r3_0,c3_0,r3_0+M-1,c3_0+M-1

def find_connect(r3_0,c3_0,r3_1,c3_1):
    global N,M
    redge = [r3_1 + 1, r3_0 - 1, r3_0 - 1, r3_1 + 1]
    cedge = [c3_0 - 1, c3_1 + 1, c3_0 - 1, c3_1 + 1]
    # 벽 기준 남,북,서,동 순 순회.
    walls=[2,3,1,0]
    for i in range(4):
        r = redge[i]
        c = cedge[i]
        idx=0
        cur_wall=walls[i]
        for t in range(M):
            r += drs[i]
            c += dcs[i]
            if miji_grid[r][c] == 0:
                return (r,c,5),(M-1,idx,cur_wall)



N,M,F=map(int,input().split())
miji_grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
# NXN
# 시간의 벽 3
# 탈출구 4

wall_grid=[]
for d in range(5):
    wall_grid.append([
        list(map(int,input().split()))
        for _ in range(M)
    ])
# MxM 5개
# 동 [0]  서 [1]  남 [2]  북 [3]  위 [4]
# 위[4] 에는 4로 타임머신 위치.

grid=wall_grid
grid.append(miji_grid)
#print(grid[5])
#print(miji_grid)
#print(grid[4])

strange_event=[
    list(map(int,input().split()))
    for _ in range(F)
]
# r,c , v, d 가 F개.
# (r,c) 좌표, v: 배수 턴, d: 방향 (배수 턴마다 한칸씩 확산됨)

#print(miji_grid)
#print(wall_grid)
#print(strange_event)

NOW_MAP = 4  # 0,1,2,3: 벽 옆면 4: 벽 위 5: 바닥

# miji_grid에서 3과 맞닿은 0 찾기.
# #MxM좌표 얻고, M-1~M+1 범위 탐색.(귀퉁이 제외) -> 하나만 0일것.
r3_0,c3_0,r3_1,c3_1=find_3_in_miji()

# print(r3_0,c3_0,r3_1,c3_1)
connection_miji,connection_wall=find_connect(r3_0,c3_0,r3_1,c3_1)
# print(connection_miji,connection_wall)

#bfs를 위한 visited. 0~4: 벽, 5: 미지의 공간
visited=[]
for d in range(5):
    visited.append([[False]*M for _ in range(M)])
visited.append([[False]*N for _ in range(N)])
#print(visited)

distance=[]
for d in range(5):
    distance.append([[-1]*M for _ in range(M)])
distance.append([[-1]*N for _ in range(N)])
turn_events = dict()
turn_events[0] = list((r, c, 5) for r, c, d, v in strange_event)
#시작점 구하기
start_r,start_c,start_map=find_start()

ANSWER=-1
#print(find_start())
bfs(start_r,start_c,start_map)
print(ANSWER)
#print(turn_events)
#print_grid(distance)
#print_grid(visited)





#print(in_grid(7,8,5))
#bfs(0,0,4)
#print(visited[4])
#print(distance[4])
#print(wall_grid[4])

#event_process(0)
#print(strange_event)
#print(grid[5])
#event_process(1)
#print(strange_event)
#event_process(14)
#print(strange_event)
#print(grid[5])


