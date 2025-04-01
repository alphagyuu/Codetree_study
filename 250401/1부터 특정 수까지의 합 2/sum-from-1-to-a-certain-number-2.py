n=int(input())
def sigma(n):
    if n==0:
        return 0
    return sigma(n-1)+n
print(sigma(n))