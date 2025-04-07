N=int(input())
dots=[
    list(map(int,input().split()))
    for _ in range(N)
]
xs=set([x for x,y in dots])
ys=set([y for x,y in dots])
xys=[x for x in xs]+[y for y in ys]

valid=0
for i in range(len(xys)):
    for j in range(i+1,len(xys)):
        for k in range(j+1,len(xys)):
            l=[['o','o']]*3
            for idx,x in enumerate ((i,j,k)):
                if x<len(xs):
                    l[idx][0]=xys[x]
                else:
                    l[idx][1]=xys[x]
            cnt=0
            for dot in dots:
                for line in l:
                    if dot[0]==line[0] or dot[1]==line[1]:
                        cnt+=1
            if cnt==len(dots):
                valid=1

print(valid)
