def dec(n):
    return((n%100)//10)
arr=list(map(int,input().split()))
darr=[dec(a) for a in arr if a>9]
for i in range(1,10):
    print(f"{i} - {darr.count(i)}")