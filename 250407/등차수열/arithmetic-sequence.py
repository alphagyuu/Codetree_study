N=int(input())
nums=list(map(int,input().split()))
max_cnt=0
for k in range(min(nums),max(nums)+1):
    cnt=0
    for i in range(1,((max(nums)-min(nums))//2)+2):
        if k-i in nums and k+i in nums:
            cnt+=1
    if cnt>max_cnt:
        max_cnt=cnt
print(max_cnt)