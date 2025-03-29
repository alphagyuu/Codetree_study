n=int(input())
arr= [
    [0 for i in range(n)]
    for i in range(n)
]

def val(i,j):
    if i==0 or j==0:
        return(1)
    else:
        return(arr[i-1][j]+arr[i][j-1]+arr[i-1][j-1])

for i in range(n):
    for j in range(n):
        arr[i][j]=val(i,j)

for i in range(n):
    print(*arr[i])