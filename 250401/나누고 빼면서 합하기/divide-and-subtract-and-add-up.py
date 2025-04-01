ln,m=map(int,input().split())
a=list(map(int,input().split()))
def cal(m):
    if m%2==1:
        return m-1
    else:
        return m//2
tot=0
while m>0:
    tot+=a[m-1]
    m=cal(m)
print(tot)