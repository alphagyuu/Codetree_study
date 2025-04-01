a=input()
def check(a):
    if len(set(list(a)))>=2:
        print("Yes")
    else:
        print("No")
check(a)