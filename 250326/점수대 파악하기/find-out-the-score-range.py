arr=list(map(int,input().split()))
caar=[]
for a in arr:
    if a==0:
        break
    elif a>9:
        caar.append(a//10)

for i in range(10,0,-1):
    print(f"{i*10} - {caar.count(i)}")
