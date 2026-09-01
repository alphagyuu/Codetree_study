n, k = map(int,input().split())

arr = list(map(int,input().split()))

psum = [arr[0]]*n

for i in range(1,n):
    psum[i] = psum[i-1] + arr[i]

ans = 0

for i in range(k,n):
    ans = max(ans, psum[i]-psum[i-k])

print(ans)