a,o,c=map(str,input().split())
an=int(a)
cn=int(c)
def cal(o):
    if o=="+":
        return(an+cn)
    elif o=="-":
        return(an-cn)
    elif o=="*":
        return(an*cn)
    elif o=="/":
        return(an//cn)
    else:
        return False
if not cal(o):
    print("False")
else:
    print(f"{a} {o} {c} = {cal(o)}")