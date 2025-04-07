N,M=map(int,input().split())
nums=list(map(int,input().split()))


for limit in range(max(nums),sum(nums)):
    bars=0
    cur=0
    max_part=0
    for n in nums:
        if cur+n<=limit:
            cur+=n
        else:
            bars+=1
            if max_part<cur:
                max_part=cur
            cur=n
    if bars<=M-1:
        print(max_part)
        break
        