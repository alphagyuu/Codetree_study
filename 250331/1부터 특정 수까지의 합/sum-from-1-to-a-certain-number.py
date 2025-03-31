n=int(input())
def f(n):
    out=0
    for i in range(n):
        out+=(i+1)
    return out//10
print(f(n))