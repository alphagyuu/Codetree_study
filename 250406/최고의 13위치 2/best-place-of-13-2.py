N=int(input())

pan=[
    list(map(int,input().split()))
    for _ in range(N)
]
idx=0
smallboxes=[]
for r in range(N):
    for c in range(N-2):
        smallboxes.append([idx,sum(pan[r][c:c+3])])
        idx+=1
    idx+=2
smallboxes.sort(key=lambda x:x[1],reverse=True)
def loop():
    for i in range(len(smallboxes)):
        for j in range(i+1,len(smallboxes)):
            if abs(smallboxes[i][0]-smallboxes[j][0])>2:
                return smallboxes[i][1]+smallboxes[j][1]
    return 0
print(loop())
#print(smallboxes)
