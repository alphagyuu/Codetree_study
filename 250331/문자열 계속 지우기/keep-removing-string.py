a=input()
b=input()
while b in a:
    idx=a.index(b)
    a=a[:idx]+a[idx+len(b):]
print(a)