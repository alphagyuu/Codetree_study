n=int(input())
arr=[1]
def next(arr):
    temp=[]
    for i in range(len(arr)+1):
        if i==0 or i==len(arr):
            temp.append(1)
        else:
            temp.append(arr[i-1]+arr[i])
    return temp
for i in range(n):
    print(*arr)
    arr=next(arr)