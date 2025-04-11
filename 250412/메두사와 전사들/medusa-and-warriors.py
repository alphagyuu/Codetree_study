# 04/11 22:00
from collections import deque


dr_UDLR=[-1,1,0,0]
dc_UDLR=[0,0,-1,1]

dr_LRUD=[0,0,-1,1]
dc_LRUD=[-1,1,0,0]

def print_2d_arr(arr):
    for rows in arr:
        print(*rows)

def in_grid(r,c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

def mds_bfs(Sr,Sc):
    mds_q=deque()
    mds_visited[Sr][Sc]=True
    mds_distance[Sr][Sc]=0
    mds_q.append((Sr,Sc))
    while mds_q:
        cur_r,cur_c=mds_q.popleft()
        for (dr,dc) in zip(dr_UDLR,dc_UDLR):
            new_r,new_c=cur_r+dr,cur_c+dc
            if in_grid(new_r,new_c):
                if grid[new_r][new_c]==0 and mds_visited[new_r][new_c]==False:
                    mds_visited[new_r][new_c]=True
                    mds_distance[new_r][new_c]=mds_distance[cur_r][cur_c]+1
                    mds_before_r_c[(new_r,new_c)]=(cur_r,cur_c)
                    mds_q.append((new_r,new_c))
                if (new_r,new_c)==(Er,Ec):
                    mds_distance[new_r][new_c] = mds_distance[cur_r][cur_c] + 1
                    return

def mds_path(T):
    global Er,Ec
    r,c=Er,Ec
    for _ in range(T):
        r,c=mds_before_r_c[(r,c)]
        MDS_PATH.appendleft((r,c))
    return




def mds_sight(mds_r,mds_c):
    stone_warriors=[[] for _ in range(4)]
    sight=[[] for _ in range(4)]
    for i,dr_main,dc_main in zip(range(4),dr_UDLR,dc_UDLR):
        #print(i,dr_main,dc_main)
        sight_visited = [[False] * N for _ in range(N)]
        if dc_main==0: #상,하
            r,c = mds_r+dr_main, mds_c
            # 직진
            not_yet=True
            while not_yet:
                if not in_grid(r,c) or sight_visited[r][c]==True:
                    break
                warrior_num=SIGHT_GRID[r][c]
                sight_visited[r][c]=True
                sight[i].append((r,c))
                if warrior_num!="X":
                    stone_warriors[i].append(warrior_num)
                    while True:
                        r+=dr_main
                        if in_grid(r,c):
                            sight_visited[r][c]=True
                        else:
                            break
                    not_yet = False
                r += dr_main
            # dc = -1 방향
            for j in range(1,mds_c+1):
                r,c=mds_r+dr_main*j,mds_c-j
                while True:
                    if not in_grid(r, c) or sight_visited[r][c] == True:
                        break
                    warrior_num = SIGHT_GRID[r][c]
                    sight_visited[r][c] = True
                    sight[i].append((r, c))
                    if warrior_num != "X":
                        stone_warriors[i].append(warrior_num)
                        for k in range(1, c + 1):
                            r, c = r + dr_main * k, c - k
                            while True:
                                if in_grid(r,c):
                                    sight_visited[r][c] = True
                                else:
                                    break
                                r += dr_main
                    r += dr_main
            # dc = 1 방향
            for j in range(1,N-mds_c):
                r,c=mds_r+dr_main*j,mds_c+j
                while True:
                    if not in_grid(r, c) or sight_visited[r][c] == True:
                        break
                    warrior_num = SIGHT_GRID[r][c]
                    sight_visited[r][c] = True
                    sight[i].append((r, c))
                    if warrior_num != "X":
                        stone_warriors[i].append(warrior_num)
                        for k in range(1, N-c):
                            r, c = r + dr_main * k, c + k
                            while True:
                                if in_grid(r,c):
                                    sight_visited[r][c] = True
                                else:
                                    break
                                r += dr_main
                    r += dr_main

        #좌우도 똑같이
        if dr_main==0: #좌,우
            r,c = mds_r, mds_c+dc_main
            # 직진
            not_yet=True
            while not_yet:
                if not in_grid(r,c) or sight_visited[r][c]==True:
                    break
                warrior_num=SIGHT_GRID[r][c]
                sight_visited[r][c]=True
                sight[i].append((r,c))
                if warrior_num!="X":
                    stone_warriors[i].append(warrior_num)
                    while True:
                        c+=dc_main
                        if in_grid(r,c):
                            sight_visited[r][c]=True
                        else:
                            break
                    not_yet = False
                c += dc_main
            # dr = -1 방향
            for j in range(1,mds_r+1):
                r,c=mds_r-j,mds_c+dc_main*j
                while True:
                    if not in_grid(r, c) or sight_visited[r][c] == True:
                        break
                    warrior_num = SIGHT_GRID[r][c]
                    if not sight_visited[r][c]:
                        sight_visited[r][c] = True
                        sight[i].append((r, c))
                    if warrior_num != "X":
                        stone_warriors[i].append(warrior_num)
                        for k in range(1, r + 1):
                            r, c = r - k, c + dc_main * k
                            #print("으아",warrior_num, r, c)
                            while True:
                                if in_grid(r,c):
                                    sight_visited[r][c] = True
                                else:
                                    break
                                c += dc_main
                    c += dc_main
            # dr = 1 방향
            for j in range(1,N-mds_r):
                r,c=mds_r+j,mds_c+dc_main*j
                while True:
                    if not in_grid(r, c) or sight_visited[r][c] == True:
                        break
                    warrior_num = SIGHT_GRID[r][c]
                    sight_visited[r][c] = True
                    sight[i].append((r, c))
                    if warrior_num != "X":
                        stone_warriors[i].append(warrior_num)
                        for k in range(1, N-r):
                            r, c = r + k, c + dc_main * k
                            while True:
                                if in_grid(r,c):
                                    sight_visited[r][c] = True
                                else:
                                    break
                                c += dc_main
                    c += dc_main


        #print(stone_warriors[i])
        #print(sight[i])
    stone_nums=[len(x) for x in stone_warriors]
    sight_idx=stone_nums.index(max(stone_nums))
    #print(sight_idx)
    return sight_idx,sight[sight_idx],stone_warriors[sight_idx],stone_nums[sight_idx]



def manhat(r,c):
    global mds_r,mds_c
    return abs(mds_r-r)+abs(mds_c-c)


N,M = map(int,input().split())
Sr,Sc,Er,Ec= map(int,input().split())
#print(N,M)
#print(Sr,Sc,Er,Ec)

input_warriors=list(map(int,input().split()))
#warriors=[[] for _ in range(M)]
warriors=dict()
for i in range(len(input_warriors)//2):
    warriors[i]=(input_warriors[i*2],input_warriors[i*2+1])

#print(input_warriors)
#print(warriors)
stone_warriors=[False*M]

grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
mds_visited=[[False]*N for _ in range(N)]
mds_distance=[[-1]*N for _ in range(N)]
#print(grid)

mds_before_r_c = dict()
mds_bfs(Sr,Sc)
#print_2d_arr(mds_visited)
#print_2d_arr(mds_distance)
#print(mds_before_r_c)
TOTAL_TURNS=mds_distance[Er][Ec]-1
#print(TOTAL_TURNS)
MDS_PATH=deque()
mds_path(TOTAL_TURNS)
#print(MDS_PATH)
#print_2d_arr(mds_distance)
#for _ in range(TOTAL_TURNS):
#    print(MDS_PATH.popleft())
SIGHT_GRID = [["X"] * N for _ in range(N)]
for i in range(M):
    if i in warriors:
        r, c = warriors[i]
        SIGHT_GRID[r][c] = i
#print_2d_arr(SIGHT_GRID)
for turn in range(TOTAL_TURNS):
    SIGHT_GRID = [["X"] * N for _ in range(N)]
    for i in range(M):
        if i in warriors:
            r, c = warriors[i]
            SIGHT_GRID[r][c] = i
    MOVES0 = 0
    ATTACKS2 = 0
    #print(turn)
    mds_r,mds_c=MDS_PATH.popleft()
    #print("메두사:",mds_r,mds_c)
    for i in range(M):
        if i not in warriors:
            continue
        if warriors[i]==(mds_r,mds_c):
            warriors.pop(i)
            #ATTACKS2+=1 #이건 메두사가 전사를 공격한거임.
    SIGHT_DIR,SIGHT_rcs,STONES,STONE_NUM1=mds_sight(mds_r,mds_c)
    #print(SIGHT_rcs)
    #print(STONES)
    #print(warriors)
    for i in range(M):
        if i not in warriors:
            continue
        if i not in STONES: # 돌이면 스킵.
            (wr,wc)=warriors[i]
            new_wr=-1
            new_wc=-1
            manhat_dis_original=manhat(wr,wc)
            manhat_dis=[]
            for dir in range(4):
                if ((wr+dr_UDLR[dir],wc+dc_UDLR[dir]) in SIGHT_rcs):
                    manhat_dis.append(manhat_dis_original+1)
                else:
                    manhat_dis.append(manhat(wr+dr_UDLR[dir],wc+dc_UDLR[dir]))
            #print(i,manhat_dis_original,manhat_dis)
            dir=manhat_dis.index(min(manhat_dis))
            if min(manhat_dis)<manhat_dis_original: #거리 못줄이면 스킵.
                new_wr=wr+dr_UDLR[dir]
                new_wc=wc+dc_UDLR[dir]
                if in_grid(new_wr,new_wc) and (new_wr,new_wc) not in SIGHT_rcs:
                    warriors[i]=(new_wr,new_wc)
                    MOVES0+=1
                if (new_wr,new_wc)==(mds_r,mds_c):
                    ATTACKS2+=1
                    warriors.pop(i)
                    continue
                else:
                    (wr,wc)=warriors[i]
                    manhat_dis_original=manhat(wr,wc)
                    manhat_dis=[]
                    for dir in range(4):
                        if ((wr+dr_LRUD[dir],wc+dc_LRUD[dir]) in SIGHT_rcs):
                            manhat_dis.append(manhat_dis_original + 1)
                        else:
                            manhat_dis.append(manhat(wr+dr_LRUD[dir],wc+dc_LRUD[dir]))
                    #print(manhat_dis_original,manhat_dis)
                    dir=manhat_dis.index(min(manhat_dis))
                    if min(manhat_dis)<manhat_dis_original: #거리 못줄이면 스킵.
                        new_wr=wr+dr_LRUD[dir]
                        new_wc=wc+dc_LRUD[dir]
                        if in_grid(new_wr,new_wc) and (new_wr,new_wc) not in SIGHT_rcs:
                            warriors[i]=(new_wr,new_wc)
                            MOVES0+=1
                        if (new_wr,new_wc)==(mds_r,mds_c):
                            ATTACKS2+=1
                            warriors.pop(i)
    #print(warriors)
    print(MOVES0,STONE_NUM1,ATTACKS2)

print(-1 if TOTAL_TURNS<0 else 0)

#print(mds_sight(2,4))
# returns sight_idx,sight[sight_idx],stone_warriors[sight_idx],stone_nums[sight_idx]