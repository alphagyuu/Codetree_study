arr = list(map(int, input().split(" ")))

tot=0
cnt=0
for a in arr:
    if a>=250:
        break
    tot+=a
    cnt+=1
avg=tot/cnt
print(f"{tot} {avg:.1f}")
