word=input()
tot=0
for a in word:
    if ord(a)>=ord("0") and ord(a)<=ord("9"):
        tot+=int(a)
print(tot)