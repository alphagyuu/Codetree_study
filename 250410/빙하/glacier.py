from collections import deque


drs=[1,0,-1,0]
dcs=[0,1,0,-1]

def in_grid(r,c):
    global N,M
    if 0 <= r < N and 0 <= c < M:
        return True
    return False

def is_effective(r,c):
    for i in range(4):
        newr=r+drs[i]
        newc=c+dcs[i]
        if in_grid(newr,newc):
            if grid[newr][newc]==0:
                return True
    return False

def melt():
    #effective_waters를 모두 꺼내서, 다음 단게 유효한 물들로 채움.
    for _ in range(len(effective_waters)):
        curr,curc=effective_waters.popleft()
        for dir_i in range(4):
            newr=curr+drs[dir_i]
            newc=curc+dcs[dir_i]
            if in_grid(newr,newc):
                if not visited[newr][newc]:
                    visited[newr][newc]=True
                    global VISITED_WATERS
                    VISITED_WATERS+=1
                    effective_waters.append((newr,newc))
                    if (newr,newc) in useless_waters:
                        useless_waters.remove((newr,newc))
                    # 해야하지만 성능 구림 -> 차라리 매 턴마다 순회하면서 없애기..?



N,M=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
visited=[
    [False]*M for _ in range(N)
] # visited 처럼 사용 가능.
effective_waters=deque()
useless_waters=deque() # NxM일 필요가 없을지도.
# 매 초마다 **녹이기**
# **유효한 물의 위치** 필요
# **유효한 물[0]**의 **인접 빙하[1]**을 0으로 변경.
# -> 모두 0이되면 그 직전 빙하 개수 필요.

# INSIGHT
# N,M이 작으므로 여러 배열을 통ㅇ해 정보 저장 가능할듯.
# 유효하지 않았다가 유효해질 수 있음.
# 한번 유효하면 계속 유효, 유효한 물로부터 만들어진 물은 무조건 유효.

# 직전 빙하를 일일히 세지 말고. VISITED_WATERS에 방문할때마다 1씩 증가를 시키고,
# -> 이전 len(useless)+VISITED 값을 전체에서 빼서 계산하자.

# [유효한 물]
# [유효하지 않은 물]
# 두 배열을 통해 관리하자!
VISITED_WATERS=0
for r in range(N):
    for c in range(M):
        if grid[r][c]==0:
            if is_effective(r,c):
                visited[r][c]=True
                VISITED_WATERS+=1
                effective_waters.append((r,c))
            else:
                useless_waters.append((r,c))

#print(effective_waters)
#print(useless_waters)
#print(N * M - len(useless_waters) - VISITED_WATERS)
TIME=0
GLACIERS=N * M - len(useless_waters) - VISITED_WATERS
while True:
    melt()
    TIME+=1
    if (N * M - len(useless_waters) - VISITED_WATERS)==0:
        print(TIME,GLACIERS)
        break
    else:
        GLACIERS = N * M - len(useless_waters) - VISITED_WATERS
