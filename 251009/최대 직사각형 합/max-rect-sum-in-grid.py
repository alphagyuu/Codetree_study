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
        inner_rows=[0]
        for i in range(1,N+1):
            inner_rows.append(prefix_sums[x2][i]-prefix_sums[x1-1][i]-prefix_sums[x2][i-1]+prefix_sums[x1-1][i-1])
        cur_sum = inner_rows[1]
        max_sum = inner_rows[1]
        for i in range(2,N+1):
            cur_sum = max(cur_sum+inner_rows[i],inner_rows[i])
            max_sum = max(cur_sum,max_sum)
        max_box = max(max_box,max_sum)
print(max_box)