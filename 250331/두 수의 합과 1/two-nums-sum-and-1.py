a,b=map(int,input().split())
s=str(a+b)
tot=0
for x in s:
    if x=="1":
        tot+=1
print(tot)