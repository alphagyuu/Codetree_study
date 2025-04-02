m1,d1,m2,d2=map(int,input().split())
def days_in_month(m):
    if m==2:
        return(28)
    elif m<8 and m%2==1:
        return(31)
    elif m>7 and m%2==0:
        return(31)
    else:
        return(30)

months=[days_in_month(i+1) for i in range(12)]

def date(m,d):
    return sum(months[0:m-1])+d

yo=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

print(yo[(date(m2,d2)-date(m1,d1))%7])

