a=int(input())
arr=[i+1 for i in range(a) if not (((i+1)%2==0 and (i+1)%4!=0) or ((i+1)//8)%2==0 or ((i+1)%7)<4)]
print(*arr)