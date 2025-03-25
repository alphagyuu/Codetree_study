y=int(input())
print("false" if y%4!=0 or (y%100==0 and y%400!=0) else "true")