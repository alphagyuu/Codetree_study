ln,lm,k=map(int,input().split())
students=[0]*(ln+1)
for _ in range(lm):
    n=int(input())
    students[n]+=1
    if students[n]>=k:
        print(n)
        break