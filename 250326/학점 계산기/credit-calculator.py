l=int(input())
arr=list(map(float,input().split()))
avg=sum(arr)/l
print(f"{avg:.1f}")
print("Perfect" if avg>=4.0 else ("Poor" if avg<3.0 else "Good"))