b=list(str(input()))
lb=len(b)
out=0
for i in range(lb):
    out+=(2**i)*int(b.pop())
print(out)
