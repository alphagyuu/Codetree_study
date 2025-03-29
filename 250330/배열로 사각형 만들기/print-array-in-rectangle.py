arr= [
    [0 for i in range(5)]
    for i in range(5)
]

def val(i,j):
    if i==0 or j==0:
        return(1)
    else:
        return(arr[i-1][j]+arr[i][j-1])

for i in range(5):
    for j in range(5):
        arr[i][j]=val(i,j)

for i in range(5):
    print(*arr[i])