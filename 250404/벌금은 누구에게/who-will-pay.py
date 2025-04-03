ln,lm,k=map(int,input().split())
students=[0]*(ln+1)
find=False
for _ in range(lm):
    n=int(input())
    students[n]+=1
    if students[n]>=k:
        print(n)
        find=True
        break
if not find:
    print(-1)