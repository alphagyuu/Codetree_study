N=int(input())
dots=[
    tuple(map(int,input().split()))
    for _ in range(N)
]
max_size=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if dots[i]!=dots[j] and dots[j]!=dots[k] and dots[k]!=dots[i]:
                xy=list(zip(dots[i],dots[j],dots[k]))
                ds=[dots[i],dots[j],dots[k]]
                if len(set(xy[0]))==2 and len(set(xy[1]))==2:
                    ds.sort(key=lambda x:(x[0],x[1]))
                    if ds[0][0]==ds[1][0]:
                        y_=ds[1][1]-ds[0][1]
                        x_=ds[2][0]-ds[1][0]
                    else:
                        y_=ds[2][1]-ds[1][1]
                        x_=ds[1][0]-ds[0][0]
                    if max_size<x_*y_:
                        max_size=x_*y_

print(max_size)