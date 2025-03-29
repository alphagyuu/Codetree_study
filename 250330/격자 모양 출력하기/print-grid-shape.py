n,m=map(int,input().split())
point_pos=[
    list(map(int,input().split()))
    for _ in range(m)
]
grid=[
    [0 for j in range(n)]
    for i in range(n)
]
for point in point_pos:
    grid[point[0]-1][point[1]-1]=point[0]*point[1]

for i in range(n):
    print(*grid[i])