n=int(input())
# return value
def a(n):
    if n==1 or n==2:
        return n
    else:
        return a(n//3)+a(n-1)
print(a(n))