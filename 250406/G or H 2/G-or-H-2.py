N=int(input())
people=[
    map(str,input().split())
    for _ in range(N)
]
people=[[int(x),A] for x,A in people]
people.sort(key=lambda x:x[0])
front=0
end=0
photos=[]
for i in range(len(people)):
    front=people[i][0]
    j=i
    gs=0
    hs=0
    while j<len(people):
        end=people[j][0]
        if people[j][1]=="G":
            gs+=1
        else:
            hs+=1
        if gs==hs or gs==0 or hs==0:
            photos.append(end-front)
        j+=1
print(max(photos))
