a=input()
b=input()
for i in range(len(b)):
    a=a[-1]+a[:-1]
    if(a==b):
        print(i+1)
        break
if (a!=b):
    print(-1)
