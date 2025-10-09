N,K=map(int,input().split())

ns=[[0]*(N+1)]

prefix_sums=[[0]*(N+1) for _ in range(N+1)]

for _ in range(N):
    ns.append([0]+list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,N+1):
        prefix_sums[i][j] = ns[i][j] + prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1]

maxbox=0

for i in range(1,N+1-(K-1)):
    for j in range(1,N+1-(K-1)):
        boxsum = prefix_sums[i+K-1][j+K-1] - prefix_sums[i+K-1][j-1] - prefix_sums[i-1][j+K-1] + prefix_sums[i-1][j-1]
        maxbox = max(maxbox,boxsum)

print(maxbox)