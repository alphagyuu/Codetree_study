N,T=map(int,input().split())
R,C,D=map(str,input().split())
R=int(R)
C=int(C)
d=0
if D=="U" or D=="D":
    d= -1 if D=="U" else 1
    for i in range(T):
        if R==1 and D=="U":
            d=1
            D="D"
        elif R==N and D=="D":
            d=-1
            D="U"
        else:
            R+=d
if D=="R" or D=="L":
    d= -1 if D=="L" else 1
    for i in range(T):
        if C==1 and D=="L":
            d=1
            D="R"
        elif C==N and D=="R":
            d=-1
            D="L"
        else:
            C+=d
print(R,C)


