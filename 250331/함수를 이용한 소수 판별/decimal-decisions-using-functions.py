a,b=map(int,input().split())
primes=[2]
for i in range(3,b+1):
    is_p=True
    for p in primes:
        if i%p==0:
            is_p=False
            break
    if is_p:
        primes.append(i)
p_in_range=[p for p in primes if p>=a and p<=b]
print(sum(p_in_range))