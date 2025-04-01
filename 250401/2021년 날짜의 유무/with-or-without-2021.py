m,d=map(int,input().split())
def in2021(m,d):
    if m<1 or m>12:
        return("No")
    elif m==2:
        if d>0 and d<=28:
            return("Yes")
        else:
            return("No")
    elif (m<8 and m%2==1) or (m>=8 and m%2==0):
        if d>0 and d<=31:
            return("Yes")
        else:
            return("No")
    else:
        if d>0 and d<=30:
            return("Yes")
        else:
            return("No")
    return("No")
print(in2021(m,d))