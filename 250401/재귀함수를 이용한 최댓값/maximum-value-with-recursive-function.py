ln=int(input())
nums=list(map(int,input().split()))
def jjang(n):
    if n==1:
        return nums[0]
    return max(jjang(n-1),nums[n-1])
print(jjang(ln))
