n=int(input())
def loop(n):
    for i in range(2,n):
        if n%i==0:
            return("C")
    return("P")
print(loop(n))