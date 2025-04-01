a,b=map(int,input().split())
def f(a,b):
    if a>b:
        a+=25
        b*=2
    else:
        a*=2
        b+=25
    return(a,b)
a,b=f(a,b)
print(a,b)