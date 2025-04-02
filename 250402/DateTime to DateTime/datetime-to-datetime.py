a,b,c=map(int,input().split())
def bun(d,h,m):
    return (d*60*24+h*60+m)
print(bun(a,b,c)-bun(11,11,11))