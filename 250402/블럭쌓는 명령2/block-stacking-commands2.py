ln,k=map(int,input().split())
insts=[
    list(map(int,input().split()))
    for i in range(k)
]
train=[0]*ln
for inst in insts:
    for i in range(inst[0]-1,inst[1]):
        train[i]+=1
print(max(train))