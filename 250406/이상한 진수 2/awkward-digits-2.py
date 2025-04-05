N=[int(x) for x in list(input())]
if 0 in N:
    N[N.index(0)]=1
else:
    N[-1]=0
N.reverse()
i=1
out=0
for n in N:
    out+=i*n
    i*=2
print(out)