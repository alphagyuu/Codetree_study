ln,t = map(int,input().split())
nums=list(map(int,input().split()))
combo=0
best=0
for n in nums:
    if n>t:
        combo+=1
    else:
        combo=0
    if best<combo:
        best=combo
print(best)