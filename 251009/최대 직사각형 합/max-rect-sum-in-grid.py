N = int(input())

ns = [[0]*(N+1)]

for _ in range(N):
    ns.append([0]+list(map(int,input().split())))

prefix_sums = [[0]*(N+1) for _ in range(N+1)]



for i in range(1,N+1):
    for j in range(1,N+1):
        prefix_sums[i][j] = ns[i][j] + prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1]

max_box=(-1000)*(N**2)

for x2 in range(1,N+1):
    for x1 in range(1,x2+1):
        for y2 in range(1,N+1):
            for y1 in range(1,y2+1):
                box_sum = prefix_sums[x2][y2] - prefix_sums[x1-1][y2] - prefix_sums[x2][y1-1] + prefix_sums[x1-1][y1-1]
                max_box = max(box_sum,max_box)

print(max_box)