s1,s2=map(str,input().split())
l1=len(s1)
l2=len(s2)
if(l1==l2):
    print("same")
elif(l1>l2):
    print(f"{s1} {l1}")
else:
    print(f"{s2} {l2}")