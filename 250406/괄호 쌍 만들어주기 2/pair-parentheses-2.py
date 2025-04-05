a=input()
before=a[0]
f=[]
b=[]
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        if a[i]=="(":
            f.append(i)
        else:
            b.append(i)
cnt=0
for x in f:
    for y in b:
        if x<y:
            cnt+=1
print(cnt)
