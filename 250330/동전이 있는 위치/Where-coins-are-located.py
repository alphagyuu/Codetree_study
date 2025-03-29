n,m=map(int,input().split())
coin_pos=[list(map(int,input().split())) for i in range(m)]
grid=[
    [0 for j in range(n)]
    for i in range(n)
]
for coin in coin_pos:
    grid[coin[0]-1][coin[1]-1]=1

for i in range(n):
    print(*grid[i])
