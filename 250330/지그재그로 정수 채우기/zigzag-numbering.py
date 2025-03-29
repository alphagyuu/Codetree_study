n=int(input())
arr=[
    [0]*n
    for _ in range(n)
]
cnt=1
for j in range(n):
    if(j%2==0):
        for i in range(n):
            arr[n-i-1][-j-1]=cnt
            cnt+=1
    else:
        for i in range(n):
            arr[i][-j-1]=cnt
            cnt+=1
print(arr)