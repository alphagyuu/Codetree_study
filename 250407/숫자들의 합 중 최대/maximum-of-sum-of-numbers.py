x,y=map(str,input().split())

totx=0
toty=0
for i in range(len(x)):
    totx+=int(x[i])
for i in range(len(y)):
    toty+=int(y[i])
print(max(totx,toty))