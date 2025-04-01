n=int(input())
def r(n):
    if n==0:
        return 0
    return (n%10)**2+r(n//10)
print(r(n))