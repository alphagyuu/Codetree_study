ln=int(input())
nums=[
    int(input())
    for _ in range(ln)
]
nums.sort(reverse=True)

def carry_sum(i,j,k):
    ns=[i,j,k]
    j=[[],[],[],[]]
    for x in ns:
        v=nums[x]
        for i in range(4):
            j[i].append(v%10)
            v=v//10
    for hanj in j:
        if sum(hanj)>9:
            return False
    return True
            
fail=True
for i in range(ln):
    for j in range(i+1,ln):
        for k in range(j+1,ln):
            if carry_sum(i,j,k):
                print(nums[i]+nums[j]+nums[k])
                fail=False
                break
if fail:
    print(-1)