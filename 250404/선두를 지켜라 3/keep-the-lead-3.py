N,M=map(int,input().split())
arun=[
    list(map(int,input().split()))
    for _ in range(N)
]
brun=[
    list(map(int,input().split()))
    for _ in range(M)
]
pa=0
pb=0
aloc=0
bloc=0
hof=[0,0]
count=0
racetime=sum([t for x,t in arun])
for t in range(racetime):
    if arun[pa][1]==0:
        if pa<len(arun)-1:
            pa+=1
    aloc+=arun[pa][0]
    if pa<len(arun)-1:
        arun[pa][1]-=1
    if brun[pb][1]==0:
        if pb<len(brun)-1:
            pb+=1
    bloc+=brun[pb][0]
    if pb<len(arun)-1:
        brun[pb][1]-=1
    if aloc==bloc:
        new_hof=[1,1]
    elif aloc>bloc:
        new_hof=[1,0]
    else:
        new_hof=[0,1]
    if t==racetime-1:
        break
    if new_hof!=hof:
        count+=1
        hof=new_hof
#    print(arun[pa],brun[pb],aloc,bloc,hof)
print(count)
