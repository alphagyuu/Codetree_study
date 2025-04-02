ln=int(input())
nums=list(map(int,input().split()))
sel=[]
for i in range(len(nums)):
    sel.append(nums[i])
    if i%2==0:
        sel.sort()
        print(sel[(len(sel)//2)],end=" ")