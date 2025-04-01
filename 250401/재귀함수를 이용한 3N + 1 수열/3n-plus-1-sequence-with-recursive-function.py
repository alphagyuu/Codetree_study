n=int(input())
def r(n):
    if n==1:
        return 0
    return 1+r(n//2 if n%2==0 else n*3+1)
print(r(n))