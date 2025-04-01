ln=int(input())
nums=list(map(int,input().split()))
def gcd(a,b):
    if b==0:
        return(a)
    return(gcd(b,a%b))
def lcm(a,b):
    return((a*b)//gcd(a,b))

def list_lcm(ln):
    if ln==1:
        return nums[0]
    return lcm(list_lcm(ln-1),nums[ln-1])
print(list_lcm(ln))

