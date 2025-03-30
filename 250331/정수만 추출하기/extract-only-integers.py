a,b=map(str,input().split())
a1,b1="",""
for x in a:
    if ord(x)>=ord("0") and ord(x)<=ord("9"):
        a1+=x
    else:
        break
for x in b:
    if ord(x)>=ord("0") and ord(x)<=ord("9"):
        b1+=x
    else:
        break
print((int(a1)+int(b1)))