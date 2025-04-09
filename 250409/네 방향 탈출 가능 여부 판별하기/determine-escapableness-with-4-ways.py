from collections import deque

def can_go(r,c):
    global N,M
    if r>=0 and c>=0 and r<N and c<M:
        if grid[r][c]==1 and visited[r][c]==1:
            return True
    return False

def is_exit(r,c):
    if r==N-1 and c==M-1:
        return True
    return False

def bfs(r,c):
    queue=deque()
    visited[r][c]=0
    queue.append((r,c))
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]
    while queue:
        curr,curc=queue.pop()
        for dir_i in range(4):
            newr=curr+dr[dir_i]
            newc=curc+dc[dir_i]
            if is_exit(newr,newc):
                global CAN_EXIT
                CAN_EXIT=1
                return
            if can_go(newr,newc):
                visited[newr][newc]=0
                queue.append((newr,newc))



N,M = map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
#뱀이 있으면 0
# N rows, M cols.
visited=[[1]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        visited[r][c]=grid[r][c]
#방문할 때 1 -> 0 으로 관리
CAN_EXIT = 0
bfs(0,0)
print(CAN_EXIT)

