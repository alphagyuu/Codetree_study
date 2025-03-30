a=input()
inst=list(input())
for command in inst:
    if command=="L":
        a=a[1:]+a[0]
    else:
        a=a[-1]+a[:-1]
print(a)