A=input()
A=[a for a in A]

def shift():
    last=A[-1]
    for i in range(len(A)-1,0,-1):
        A[i]=A[i-1]
    A[0]=last

def encode():
    curc=A[0]
    curn=1
    code=""
    for i in range(1,len(A)):
        if A[i]!=curc:
            code+=(curc+str(curn))
            curc=A[i]
            curn=1
        else:
            curn+=1
    if curn>0:
        code+=(curc+str(curn))
    return len(code)

min_len=len(A)*2
for _ in range(len(A)):
    min_len=min(min_len,encode())
    shift()

print(min_len)