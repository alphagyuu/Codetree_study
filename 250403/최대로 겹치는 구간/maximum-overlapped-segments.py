ln=int(input())
lines=[
    list(map(int,input().split()))
    for i in range(ln)
]
first,last=lines[0][0],lines[0][0]+1
axis=[0]
for line in lines:
    if first>line[0]:
        axis=[0]*(first-line[0])+axis
        first=line[0]
    if last<line[1]:
        axis=axis+[0]*(line[1]-last)
        last=line[1]
    axis[line[0]-first:line[1]-first]=[x+1 for x in axis[line[0]-first:line[1]-first]]
print(max(axis))