def dec(n):
    return((n%100)//10)
arr=list(map(int,input().split()))
darr=[]
for a in arr:
    if a==0:
        break
    elif a>9:
        darr.append(dec(a))

for i in range(1,10):
    print(f"{i} - {darr.count(i)}")