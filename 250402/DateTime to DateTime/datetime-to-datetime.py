a,b,c=map(int,input().split())
def bun(d,h,m):
    return (d*60*24+h*60+m)
if a<11:
    print(-1)
elif a==11 and b<11:
    print(-1)
elif a==11 and b==11 and c<11:
    print(-1)
else:
    print(bun(a,b,c)-bun(11,11,11))