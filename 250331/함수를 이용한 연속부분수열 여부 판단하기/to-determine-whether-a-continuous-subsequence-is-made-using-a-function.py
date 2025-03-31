ln1, ln2=map(int,input().split())
alist=list(map(str,input().split()))
blist=list(map(str,input().split()))
def check(alist,blist):
    for i in range(len(alist)-len(blist)+1):
        if blist==alist[i:i+len(blist)]:
            return "Yes"
    return "No"
print(check(alist,blist))