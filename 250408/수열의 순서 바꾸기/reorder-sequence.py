"""
원하는 위치로 백 가능.
1 2 4 3
1,2,4

1 5 2 4 3
1,5,2,4
1 6 5 2 3 4

일단 국부적으로 반대인 애들까지만 하면 되는것같음.

1 2 -> 0
2 1 -> 1

1 2 3 6 [5] 4 7 -> 5

[2] 1 3 4 5 6 7 -> 1

5 6 1 3 4 2

5 6 1 2 3 4

"""

N=int(input())
nums=list(map(int,input().split()))
#nums=[1,2] # 0
#nums=[2,1] # 1

min_iters=0
if N>1:
    for i in range(len(nums)-1):
        if nums[i+1]<nums[i]:
            min_iters=i+1
print(min_iters)