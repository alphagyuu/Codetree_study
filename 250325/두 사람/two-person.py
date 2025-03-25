a=input().split(" ")
b=input().split(" ")
def verify(a):
    return 1 if int(a[0])>=19 and a[1]=="M" else 0
print(1 if verify(a)+verify(b) else 0)