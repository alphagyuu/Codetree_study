n=int(input())
def forward(n):
    if n==0:
        return
    forward(n-1)
    print(n,end=" ")

def backward(n):
    if n==0:
        return
    print(n,end=" ")
    backward(n-1)
forward(n)
print("")
backward(n)