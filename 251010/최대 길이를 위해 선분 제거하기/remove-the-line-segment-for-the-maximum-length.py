N = int(input())

lines = []
xs = []

for _ in range(N):
    x1,x2 = map(int,input().split())
    xs+=[x1,x2]
    lines.append((x1,x2))

xs.sort()
lines.sort()
x = dict()
xreal = dict()

for i in range(N*2):
    x[xs[i]] = i
    xreal[i] = xs[i]



pm1 = [0]*(N*2)

sx_2_li = dict()
ex_2_li = dict()
lines_comp = []

for i in range(N):
    x1,x2 = lines[i]
    lines_comp.append((x[x1],x[x2]))
    pm1[x[x1]] = 1
    pm1[x[x2]] = -1
    sx_2_li[x[x1]] = i
    ex_2_li[x[x2]] = i

independent_length = [0]*(N*2)

gyeop = 1
tot_length = 0

for i in range(1,N*2):
    if gyeop>0:
        tot_length+=xreal[i]-xreal[i-1]
    if gyeop==1:
        independent_length[i] = xreal[i] - xreal[i-1]
    gyeop+=pm1[i]

min_independent_line = 1000000000

for i in range(N):
    x1,x2 = lines_comp[i]
    min_independent_line = min(min_independent_line,sum(independent_length[x1:x2]))

print(tot_length-min_independent_line)