X,Y=map(int,input().split())
cnt=0
for i in range(X,Y+1):
    s=list(str(i))
    if s==s[::-1]:
        cnt+=1
print(cnt)