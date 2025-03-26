n=int(input())
cnt=0
arr=[]
i=0
while cnt<2:
    i+=1
    arr.append(i*n)
    if(i*n%5==0):
        cnt+=1
print(*arr)