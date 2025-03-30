sin=input()
sout=""
ex=""
n=0
for a in sin:
    if ex==a:
        n+=1
    elif ex=="":
        ex=a
        n+=1
    else:
        sout+=ex+str(n)
        n=1
        ex=a
if n>0:
    sout+=ex+str(n)
print(len(sout))
print(sout)