y=int(input())
def yoon(y):
    if y%100==0 and y%400!=0:
        return "false"
    elif y%4!=0:
        return "false"
    else:
        return "true"
print(yoon(y))