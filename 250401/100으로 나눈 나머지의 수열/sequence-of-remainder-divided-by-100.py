n=int(input())
def r(n):
    if n<=1:
        return 2
    return (r(n-1)*r(n-2))%100
print(r(n))