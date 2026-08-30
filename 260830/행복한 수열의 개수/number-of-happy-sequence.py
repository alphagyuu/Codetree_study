n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    combo = 1
    prev = 0
    for j in range(n):
        if arr[i][j] == prev:
            combo +=1
        else:
            combo = 1
        prev = arr[i][j]
        if combo >= m:
            ans+=1
            break

for i in range(n):
    combo = 1
    prev = 0
    for j in range(n):
        if arr[j][i] == prev:
            combo +=1
        else:
            combo = 1
        prev = arr[j][i]
        if combo >= m:
            ans+=1
            break
print(ans)