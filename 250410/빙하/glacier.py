from collections import deque

# 입력 받기
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 이동 (BFS용)
drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]

def in_grid(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    # (0,0)은 항상 물이므로 외부 물의 시작점이 됨.
    q.append((0, 0))
    visited[0][0] = True

    # 이번 턴에 녹일 빙하들의 좌표를 저장할 큐
    melt_queue = deque()

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + drs[i], c + dcs[i]
            if in_grid(nr, nc) and not visited[nr][nc]:
                if grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                elif grid[nr][nc] == 1:
                    # 아직 방문되지 않은 빙하를 이번 턴에 녹일 대상으로 추가
                    visited[nr][nc] = True
                    melt_queue.append((nr, nc))
    return melt_queue

time = 0
last_melt_cnt = 0

while True:
    melt_list = bfs()
    # 녹일 빙하가 없다면 종료 (빙하 전부 녹은 상태)
    if not melt_list:
        break
    last_melt_cnt = len(melt_list)
    time += 1
    # 모아둔 빙하들을 녹임 (1 -> 0 처리)
    while melt_list:
        r, c = melt_list.popleft()
        grid[r][c] = 0

print(time, last_melt_cnt)
