n=int(input())
def binary(n):
    blist=[]
    while n>1:
        blist.append(n%2)
        n//=2
    blist.append(n)
    blist.reverse()
    b="".join([str(x) for x in blist])
    return b
print(binary(n))