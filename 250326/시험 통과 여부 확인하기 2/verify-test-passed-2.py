num=int(input())
arr=[]
for i in range(num):
    arr.append(list(map(int,input().split(" "))))

answer=0
for i in range(num):
    if sum(arr[i])/4>=60:
        answer+=1
        print("pass")
    else:
        print("fail")
print(answer)
