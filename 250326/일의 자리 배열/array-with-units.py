arr=list(map(int,input().split()))
while len(arr)<10:
    arr.append(arr[-1]+arr[-2])
for a in arr:
    print(a%10,end=" ")