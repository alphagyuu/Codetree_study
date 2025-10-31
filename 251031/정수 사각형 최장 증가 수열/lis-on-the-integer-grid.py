def main():
    n = int(input())

    grid = [list(map(int,input().split())) for _ in range(n)]
    
    moves = set()

    for r in range(n):
        for c in range(n):
            moves.add((r,c))

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    def in_grid(r,c):
        return 0<=r<n and 0<=c<n

    for turn in range(1,n*n+1):
        empty = True
        next_moves = set()
        for r,c in moves:
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if not in_grid(nr,nc):
                    continue
                if grid[nr][nc] > grid[r][c]:
                    empty = False
                    next_moves.add((nr,nc))
        if empty:
            print(turn)
            return
        moves = next_moves
    print(n*n)
    return

main()