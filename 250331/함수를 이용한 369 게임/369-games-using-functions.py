a,b=map(int,input().split())
def sam(n):
    sn=str(n)
    if "3" in sn or "6" in sn or "9" in sn:
        return True
    else:
        return False
cnt=0
for n in range(a,b+1):
    if sam(n) or n%3==0:
        cnt+=1
print(cnt)