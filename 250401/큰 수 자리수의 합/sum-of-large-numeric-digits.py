a,b,c=map(int,input().split())
def jarihap(n):
    if n==0:
        return 0
    return jarihap(n//10)+n%10
print(jarihap(a*b*c))