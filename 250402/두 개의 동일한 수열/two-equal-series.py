ln=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
if set(alist)==set(blist):
    print("Yes")
else:
    print("No")