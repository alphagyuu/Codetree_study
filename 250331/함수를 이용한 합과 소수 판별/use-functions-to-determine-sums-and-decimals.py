a,b=map(int,input().split())
def jjak(n):
    sn=str(n)
    ints=[int(s) for s in sn]
    if sum(ints)%2==0:
        return True
    else:
        return False

primes=[2]
if b>3:
    for i in range(3,b+1):
        is_p=True
        for p in primes:
            if i%p==0:
                is_p=False
                break
        if is_p:
            primes.append(i)
p_in_range=[p for p in primes if p>=a and p<=b]
#print(p_in_range)
cnt=0
for p in p_in_range:
    if jjak(p):
        cnt+=1
print(cnt)