word=input()
out=""
for a in word:
    o=ord(a)
    if (o>=ord("a") and o<=ord("z")) or (o>=ord("A") and o<=ord("Z")):
        out+=(a.lower())
    elif (o>=ord("0") and o<=ord("9")):
        out+=(a)
print(out)