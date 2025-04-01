n=int(input())
def r(n):
    if n<1:
        return 0
    return n+r(n-2)
print(r(n))