from collections import deque

def can_go(r,c):
    global N,M
    if r>=0 and c>=0 and r<N and c<M:
        if grid[r][c]==1 and visited[r][c]==0:
            return True
    return False

def is_exit(r,c):
    global N,M
    if r==N-1 and c==M-1:
        return True
    return False

def bfs(r,c):
    queue=deque()
    queue.append((r,c))
    visited[r][c]=1
    length[r][c]=0
    drs=[1,0,-1,0]
    dcs=[0,1,0,-1]
    while queue:
        curr,curc=queue.popleft()
        curlength=length[curr][curc]
        for dir_i in range(4):
            newr=curr+drs[dir_i]
            newc=curc+dcs[dir_i]
            if is_exit(newr,newc):
                global PATH_LENGTH
                PATH_LENGTH=curlength+1
                return
            if can_go(newr,newc):
                visited[newr][newc]=1
                queue.append((newr,newc))
                length[newr][newc]=curlength+1



N,M = map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
#뱀이 있으면 1
# N rows, M cols.

visited=[[0]*M for _ in range(N)]
length=[[0]*M for _ in range(N)]
# 0으로 초기화.
PATH_LENGTH=0
bfs(0,0)
#print(length)
print(PATH_LENGTH)


