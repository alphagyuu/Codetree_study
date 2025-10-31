def main():
    n = int(input())

    grid = [list(map(int,input().split())) for _ in range(n)]

    moves = [set() for _ in range(n*n+1)]

    for r in range(n):
        for c in range(n):
            moves[1].add((r,c))

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    def in_grid(r,c):
        return 0<=r<n and 0<=c<n

    for turn in range(1,n*n+1):
        empty = True
        for r,c in moves[turn]:
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if not in_grid(nr,nc):
                    continue
                if grid[nr][nc] > grid[r][c]:
                    empty = False
                    moves[turn+1].add((nr,nc))
        if empty:
            print(turn)
            return
    print(n*n)
    return

main()