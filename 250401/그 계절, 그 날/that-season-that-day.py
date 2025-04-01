y,m,d=map(int,input().split())
def yoon(y):
    if y%400==0:
        return True
    elif y%100==0:
        return False
    elif y%4==0:
        return True
    else:
        return False

def val(y,m,d):
    if m==2:
        if yoon(y):
            yoond=29
        else:
            yoond=28
        if d>0 and d<=yoond:
            return True
        else:
            return False
    elif (m<8 and m%2==1) or (m>=8 and m%2==0):
        if d>0 and d<=31:
            return True
        else:
            return False
    else:
        if d>0 and d<=30:
            return True
        else:
            return False

def season(y,m,d):
    if val(y,m,d):
        if m in [3,4,5]:
            print("Spring")
        elif m in [6,7,8]:
            print("Summer")
        elif m in [9,10,11]:
            print("Fall")
        else:
            print("Winter")
    else:
        print(-1)

season(y,m,d)