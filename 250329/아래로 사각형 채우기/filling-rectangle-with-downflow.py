n=int(input())
arr=[
    [i*n+j+1 for i in range(n)]
    for j in range(n)
]
for i in range(n):
    print(*arr[i])