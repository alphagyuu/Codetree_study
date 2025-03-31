n=int(input())
def check(n):
    cn=str(n)
    cnint=[int(x) for x in cn]
    if n%2==0 and sum(cnint)%5==0:
        return "Yes"
    else:
        return "No"
print(check(n))