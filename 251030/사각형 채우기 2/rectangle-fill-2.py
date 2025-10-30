n = int(input())

f = [1]*(n+1)

f[1:3] = [1,3]

for i in range(3,n+1):
    f[i] = f[i-1] + f[i-2]*2

print(f[n])