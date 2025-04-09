from collections import deque

def can_go(r,c):
    global K
    if r>=0 and c>=0 and r<N and c<M:
        if visited[r][c]==0 and grid[r][c]>K:
            return True
    return False


def fill(r,c):
    queue=deque()
    queue.append((r,c))
    visited[r][c] = 1
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]
    while queue:
        nowr, nowc = queue.popleft()
        for diri in range(4):
            newr,newc=nowr+dr[diri],nowc+dc[diri]
            if can_go(newr,newc):
                visited[newr][newc] = 1
                queue.append((newr,newc))


N,M=map(int,input().split())
grid=[
    list(map(int,input().split()))
    for _ in range(N)
]
#grid[N][M]
#N rows, M cols.


#가장높은집을 찾아서 1~TOPK-1까지만 탐색.
TOP_K=0
for row in grid:
    if max(row)>TOP_K:
        TOP_K=max(row)
#print(TOP_K)

#K보다 낮고, 방문하지 않은 모든 지점에서 dfs 수행.
MAX_K=1 # 반드시 1이어야 함.
MAX_SAFE_AREA=0
for K in range(1,TOP_K):
    safe_areas=0
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if grid[r][c]>K and visited[r][c]==0:
                safe_areas+=1
                fill(r,c)
    if safe_areas>MAX_SAFE_AREA:
        MAX_K=K
        MAX_SAFE_AREA=safe_areas

print(MAX_K,MAX_SAFE_AREA)

