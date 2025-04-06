N=int(input())
nums=list(map(int,input().split()))
cnt=0
for i in range(N):
    for j in range(i+1,N+1):
        #print(nums[i:j])
        if sum(nums[i:j])%len(nums[i:j])==0:
            if sum(nums[i:j])//len(nums[i:j]) in nums[i:j]:
                cnt+=1
print(cnt)