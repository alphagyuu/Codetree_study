n=int(input())
def recprint(n):
    if n==0:
        return
    else:
        print("HelloWorld")
        recprint(n-1)
recprint(n)