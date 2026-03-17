N, K = map(int,input().split())

values = []

for _ in range(N):
    values.append(int(input()))

cnt = 0
for i in range(-1,-N-1,-1):
    v = values[i]
    cnt += K//v
    K %= v

print(cnt)