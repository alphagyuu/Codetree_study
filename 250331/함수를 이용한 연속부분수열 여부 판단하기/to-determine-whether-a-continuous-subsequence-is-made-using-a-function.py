ln1, ln2=map(int,input().split())
alist=list(map(str,input().split()))
blist=list(map(str,input().split()))
if "".join(blist) in "".join(alist):
    print("Yes")
else:
    print("No")