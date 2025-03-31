n=int(input())
def nn(n):
    return n+1 if n<9 else 1
def out(n):
    x=1
    for _ in range(n):
        for _ in range(n):
            print(x,end=" ")
            x=nn(x)
        print("")
out(n)