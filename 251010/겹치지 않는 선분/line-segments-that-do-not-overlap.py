MAX = 1000000
MIN = -MAX

# 겹치지 않는 조건
# (a1<b1 & a2<b2) or (a1>b1 & a2>b2) 

N = int(input())

lines = [tuple(map(int,input().split())) for _ in range(N)]

lines.sort()

lmaxes=[MIN]*(N+1)
rmins=[MAX]*(N+1)

lmax = MIN
rmin = MAX

for i in range(N):
    x1,x2 = lines[i]
    lmax = max(lmax,x2)
    lmaxes[i] = lmax

for i in range(N-1,-1,-1):
    x1,x2 = lines[i]
    rmin = min(rmin,x2)
    rmins[i] = rmin

cnt=N

for i in range(N):
    x1,x2 = lines[i]
    lmax = lmaxes[i-1]
    rmin = rmins[i+1]

    if lmax<x2 and rmin>x2:
        continue
    else:
        cnt-=1

print(cnt)