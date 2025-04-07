N=int(input())
boxes=[
    int(input())
    for _ in range(N)
]
cnt=0
avg=sum(boxes)//len(boxes)
'''
while max(boxes)>min(boxes):
    boxes[boxes.index(max(boxes))]-=1
    boxes[boxes.index(min(boxes))]+=1
    cnt+=1
시간초과
'''
for v in boxes:
    if v>avg:
        cnt+=v-avg
print(cnt)