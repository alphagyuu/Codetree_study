a=input()
part=input()
def f(part):
    if part in a:
        return a.index(part)
    else:
        return -1
print(f(part))