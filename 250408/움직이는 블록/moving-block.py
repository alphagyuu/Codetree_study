N=int(input())
boxes=[
    int(input())
    for _ in range(N)
]
cnt=0
while max(boxes)>min(boxes):
    boxes[boxes.index(max(boxes))]-=1
    boxes[boxes.index(min(boxes))]+=1
    cnt+=1
print(cnt)