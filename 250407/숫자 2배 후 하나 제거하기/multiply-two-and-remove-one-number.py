N=int(input())
nums=list(map(int,input().split()))

min_dt=sum(nums)*2
for i in range(N):
    for j in range(N):
        nums[i]*=2
        temp=nums[:j]+nums[j+1:]
        dif_tot=0
        for k in range(N-2):
            dif_tot+=abs(temp[k]-temp[k+1])
        nums[i]//=2
        if min_dt>dif_tot:
            min_dt=dif_tot
print(min_dt)