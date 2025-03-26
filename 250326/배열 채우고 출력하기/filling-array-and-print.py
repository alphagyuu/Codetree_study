arr=list(map(str,input().split(" ")))
answer=list(arr[-i-1] for i in range(len(arr)))
print("".join(answer))