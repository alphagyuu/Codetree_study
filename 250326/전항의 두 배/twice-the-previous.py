arr=list(map(int,input().split()))
while len(arr)<10:
    arr.append(arr[-1]+2*arr[-2])
print(*arr)