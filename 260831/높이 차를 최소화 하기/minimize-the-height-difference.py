from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def cango(low, high):
    if not (low <= grid[0][0] <= high):
        return False

    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()

        if r == n-1 and c == m-1:
            return True

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and low <= grid[nr][nc] <= high:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    return False


def ooh(dif):
    for low in range(1, 501-dif):
        if cango(low, low + dif):
            return True
    return False


min_dif = 0
max_dif = 499

while min_dif < max_dif:
    dif = (min_dif + max_dif) // 2

    if ooh(dif):
        max_dif = dif
    else:
        min_dif = dif + 1

print(min_dif)