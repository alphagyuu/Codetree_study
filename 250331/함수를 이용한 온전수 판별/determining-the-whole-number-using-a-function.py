a,b=map(int,input().split())
def is_o(n):
    if n%2==0:
        return False
    elif str(n)[-1]=="5":
        return False
    elif n%3==0 and n%9!=0:
        return False
    else:
        return True
os=[x for x in range(a,b+1) if is_o(x)]
print(len(os))