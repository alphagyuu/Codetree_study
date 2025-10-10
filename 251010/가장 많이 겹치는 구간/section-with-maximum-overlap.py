N=int(input())
lines=[tuple(map(int,input().split())) for _ in range(N)]

xs=[]
for x1,x2 in lines:
    xs.append(x1)
    xs.append(x2)

xs.sort()

x=dict()

for i in range(N*2):
    x[xs[i]] = i

for i in range(N):
    x1,x2 = lines[i]
    lines[i] = (x[x1],x[x2])

pm1=[0]*(N*2)

for i in range(N):
    x1,x2 = lines[i]
    pm1[x1] = 1
    pm1[x2] = -1

gyeop=0
cnt=0

for v in pm1:
    cnt+=v
    gyeop = max(gyeop,cnt)

print(gyeop)