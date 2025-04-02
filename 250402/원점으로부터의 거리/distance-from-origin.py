ln=int(input())
inputs=[
    [i+1]+list(map(int,input().split()))
    for i in range(ln)
]
points=[[x[0]]+[abs(x[1])+abs(x[2])] for x in inputs]
points.sort(key=lambda x:(x[1],x[0]))
for p in points:
    print(p[0])
