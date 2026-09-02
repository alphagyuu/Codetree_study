n = int(input())

x = {}
dots = []

for i in range(n):
    a,b = map(int,input().split())
    dots += [a,b]
    x[a] = 1
    x[b] = -1

dots.sort()

ans = 0
cur = 0
for dot in dots:
    cur += x[dot]
    ans = max(ans,cur)
    
print(ans)