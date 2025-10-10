A = input()

prev = A[-1]
rcnt = [0]*(len(A))
for i in range(1,len(A)):
    if prev ==')':
        if A[-i-1] == ')':
            rcnt[-i-1] +=1
    rcnt[-i-1] += rcnt [-i]
    prev = A[-i-1]

#print(rcnt)

prev = A[0]

cnt = 0

for i in range(1,len(A)-1):
    if prev == '(':
        if A[i] == '(':
            cnt+=rcnt[i]
    prev = A[i]

print(cnt)