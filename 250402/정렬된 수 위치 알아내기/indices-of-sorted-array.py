ln=int(input())
nums=list(map(int,input().split()))
inums=[
    [nums[i]]+[i+1]
    for i in range(len(nums))
]
inums.sort(key=lambda x:(x[0],x[1]))
sorted_i=[x[1] for x in inums]
out=[sorted_i.index(i+1)+1 for i in range(len(sorted_i))]
print(*out)

