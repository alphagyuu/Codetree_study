word=input()
out=""
for a in word:
    if ord(a)>=ord("a") and ord(a)<=ord("z"):
        out+=a.upper()
    elif ord(a)>=ord("A") and ord(a)<=ord("Z"):
        out+=a
print(out)