N = int(input())

ckpts=list(tuple(map(int,input().split())) for _ in range(N))

dists = list(abs(ckpts[i+1][1]-ckpts[i][1])+abs(ckpts[i+1][0]-ckpts[i][0]) for i in range(N-1))

dist2s = list(abs(ckpts[i+2][1]-ckpts[i][1])+abs(ckpts[i+2][0]-ckpts[i][0]) for i in range(N-2))

default_dist = sum(dists)

gain = 0

for i in range(N-2):
    gain = max(gain,-dist2s[i]+(dists[i]+dists[i+1]))

print(default_dist - gain)