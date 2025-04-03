ln=int(input())

combo=0
best=0
before="a"

for i in range(ln):
    n=int(input())
    if before==n:
        combo+=1
    else:
        combo=1
        before=n
    if combo>best:
        best=combo
print(best)