arr=[1,int(input())]
while arr[-1]<100:
    arr.append(arr[-1]+arr[-2])
print(*arr)