N,Q = map(int,input().split())

group = [[0]*(N+1) for _ in range(4)]

prefix_sums = [[0]*(N+1) for _ in range(4)]

for i in range(1,N+1):
    g = int(input())
    group[g][i] = 1

for g in range(1,4):
    for i in range(1,N+1):
        prefix_sums[g][i] = group[g][i] + prefix_sums[g][i-1]

for _ in range(Q):
    a,b = map(int,input().split())
    for g in range(1,4):
        cnt = prefix_sums[g][b] - prefix_sums[g][a-1]
        print(cnt,end = ' ')
    print('')
