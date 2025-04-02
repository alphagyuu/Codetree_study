ln=int(input())
lines=[list(map(int,input().split())) for _ in range(ln)]

axis=[0]*101

for line in lines:
    axis[line[0]:line[1]+1]=[x+1 for x in axis[line[0]:line[1]+1]]
print(max(axis))