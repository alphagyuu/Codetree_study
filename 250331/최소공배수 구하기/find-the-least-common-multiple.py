n,m=map(int,input().split())
def gcd(n,m):
    for i in range(min(n,m)):
        if n%(i+1)==0 and m%(i+1)==0:
            out=i+1
    return out
def lcm(n,m):
    return int((n*m)//(gcd(n,m)))
print(lcm(n,m))