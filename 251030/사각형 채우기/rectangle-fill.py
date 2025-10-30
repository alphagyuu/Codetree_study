n = int(input())

f = [0]*(n+1)

f[0:2] = [1,2]

for i in range(2,n+1):
    f[i] = (f[i-1]+f[i-2])%10007

print(f[n-1])