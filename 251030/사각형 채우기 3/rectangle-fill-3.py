n = int(input())

# Please write your code here.
f = [[0]*(4) for _ in range(1001)]

f[1][0] = 1
f[1][1] = 0
f[1][2] = 0
f[1][3] = 1
f[2][0] = 3
f[2][1] = 1
f[2][2] = 1
f[2][3] = 2

for i in range(3,n+1):
    for j in range(4):
        f[i][0] += f[i-1][j] + f[i-2][j]
        f[i][3] += f[i-1][j]
    for j in [1,3]:
        f[i][1] += f[i-1][j]
    for j in [2,3]:
        f[i][2] += f[i-1][j]
    

print(sum(f[n])%1000000007)