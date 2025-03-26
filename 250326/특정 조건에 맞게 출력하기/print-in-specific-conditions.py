arr=list(map(int,input().split()))
out=[]
for a in arr:
    if a==0:
        break
    elif a%2==1:
        out.append(a+3)
    else:
        out.append(a//2)
print(*out)