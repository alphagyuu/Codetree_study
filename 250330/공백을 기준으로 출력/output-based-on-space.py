s1=input()
s2=input()
s3=list(s1+s2)
while " " in s3:
    s3.remove(" ")
for s in s3:
    print(s,end='')

#s3=(s1+s2).replace(" ","")