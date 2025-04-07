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
            l=[['o','o'] for _ in range(3)]
            for idx,x in enumerate ((i,j,k)):
                if x<len(xs):
                    l[idx][0]=xys[x]
                else:
                    l[idx][1]=xys[x]
            cnt=0
            #print(i,j,k)
            #print(l)
            for dot in dots:
                #print(dot)
                inline=0
                for line in l:
                    if dot[0]==line[0] or dot[1]==line[1]:
                        inline=1
                cnt+=inline
                #print(inline)
            if cnt==len(dots):
                valid=1

print(valid)
