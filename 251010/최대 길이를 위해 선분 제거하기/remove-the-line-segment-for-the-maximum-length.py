N = int(input())

lines = []
xs = set()

for _ in range(N):
    x1,x2 = map(int,input().split())
    xs.add(x1)
    xs.add(x2)
    lines.append((x1,x2))
    
xs = list(xs)
xs.sort()
lines.sort()
x = dict()
xreal = dict()

for i in range(len(xs)):
    x[xs[i]] = i
    xreal[i] = xs[i]

lines_comp = []
pm = [0]*(len(xs))

for i in range(N):
    x1,x2 = lines[i]
    lines_comp.append((x[x1],x[x2]))
    pm[x[x1]]+=1
    pm[x[x2]]-=1

independent_length = [0]*(len(xs)) 
total_length = 0
gyeop = 0
ps_independent_length = [0]*(len(xs))

for i in range(len(xs)-1):
    gyeop += pm[i]
    part_length = xreal[i+1]-xreal[i]
    if gyeop>0:
        total_length+=part_length
    if gyeop==1:
        independent_length[i+1] = part_length
    ps_independent_length[i+1] = ps_independent_length[i] + independent_length[i+1]

min_independent_length = 1000000000

for i in range(N):
    x1,x2 = lines_comp[i]
    min_independent_length = min(min_independent_length,ps_independent_length[x2]-ps_independent_length[x1])
    #print(min_independent_length)

print(total_length - min_independent_length)