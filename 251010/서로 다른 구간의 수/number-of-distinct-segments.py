N = int(input())

lines = []
xs=[]

for _ in range(N):
    a,b = map(int,input().split())
    lines.append((a,b))
    xs+=[a,b]

xs.sort()
x=dict()

for i in range(N*2):
    x[xs[i]] = i

pm1 = [0]*(N*2)

for i in range(N):
    a,b = lines[i]
    lines[i] = (x[a],x[b])
    pm1[x[a]] = 1
    pm1[x[b]] = -1

gyeop = 0
cnt=0

for v in pm1:
    gyeop += v
    if gyeop==0:
        cnt+=1

print(cnt)