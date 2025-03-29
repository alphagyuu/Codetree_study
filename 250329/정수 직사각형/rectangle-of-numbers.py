n,m=map(int,input().split())
arr= [
    [i+1+j*m for i in range(m)]
    for j in range(n)
]
for item in arr:
    print(*item)