T,a,b=map(int,input().split())
axis=[0]*1001
for _ in range(T):
    c,x=map(str,input().split())
    x=int(x)
    axis[x]=c

tot=0
for x in range(a,b+1):
    cs=abs(x-axis.index('S'))
    cn=abs(x-axis.index('N'))
    for i in range(1,1001):
        if axis[i]=="S":
            if cs>abs(x-i):
                cs=abs(x-i)
        if axis[i]=="N":
            if cn>abs(x-i):
                cn=abs(x-i)
    if cs<=cn:
        tot+=1
print(tot)

        
            
