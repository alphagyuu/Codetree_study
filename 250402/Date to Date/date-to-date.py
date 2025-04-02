m1,d1,m2,d2=map(int,input().split())
def days_in_month(m):
    if m==2:
        return 28
    elif m<8 and m%2==1:
        return 31
    elif m>7 and m%2==0:
        return 31
    else:
        return 30
months=[days_in_month(i+1) for i in range(12)]
x1=sum(months[0:m1])+d1
x2=sum(months[0:m2])+d2
print(x2-x1)