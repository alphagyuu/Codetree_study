x1,x2,x3,x4=map(int,input().split())
'''
def loop(x1,x2,x3,x4):
    for x in range(x1,x2+1):
        if x>=x3 and x<=x4:
            return("intersecting")
    return("nonintersecting")

print(loop(x1,x2,x3,x4))
'''

if x2<x3 or x1>x4:
    print('nonintersecting')
else:
    print('intersecting')