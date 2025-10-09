from sortedcontainers import SortedSet

N,Q = map(int,input().split())

sx = SortedSet()
sy = SortedSet()

xys= list()

for _ in range(N):
    x,y = map(int,input().split())
    sx.add(x)
    sy.add(y)
    xys.append((x,y))

grid = [[0]*(N+1) for _ in range(N+1)]

prefix_sums = [[0]*(N+1) for _ in range(N+1)]

for x,y in xys:
    grid[sx.bisect_left(x)+1][sy.bisect_left(y)+1] += 1

for i in range(1,N+1):
    for j in range(1,N+1):
        prefix_sums[i][j] = grid[i][j]+prefix_sums[i-1][j]+prefix_sums[i][j-1]-prefix_sums[i-1][j-1]


for _ in range(Q):
    x1,y1,x2,y2 = map(int,input().split())
    ix2 = sx.bisect_right(x2)
    iy2 = sy.bisect_right(y2) # -1 +1
    ix1 = max(sx.bisect_left(x1),0)
    iy1 = max(sy.bisect_left(y1),0)
    cnt = prefix_sums[ix2][iy2]-prefix_sums[ix1][iy2]-prefix_sums[ix2][iy1]+prefix_sums[ix1][iy1]
    print(cnt)
