a=input()
def is_pal(word):
    if word==word[::-1]:
        return("Yes")
    else:
        return("No")
print(is_pal(a))