N,K=map(int,input().split())
people=[
    map(str,input().split())
    for _ in range(N)
]
people=[[int(x),A] for x,A in people]
people.sort(key=lambda x:x[0])
first=0
last=0
start=0
tots=[]
for i in range(N):
    start=people[i][0]
    first=i
    j=i
    tot=0
    while people[j][0]<=start+K:
        last=j
        tot+=1 if people[j][1]=="G" else 2
        j+=1
        if j>=N:
            break
    tots.append(tot)

print(max(tots))

