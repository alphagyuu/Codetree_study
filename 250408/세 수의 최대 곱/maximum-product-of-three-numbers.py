"""
1. 완전탐색 -> 불가능(시간복잡도)
2. 케이스스터디

음,양,0

양, 양/0
최댓값 3개

음/양
최솟값 2개
최댓값 1개

음,0
0포함 -> 0 (최댓값 3개에 종속)

음, 양, 0

-1 1 0 1 1 1 이러면 ㅇ

음
최댓값 3개


"""



N=int(input())
nums=tuple(map(int,input().split()))
#print(nums)

hubo=[]

ns=list(nums)
MMM=1
for _ in range(3):
    MMM*=max(ns)
    ns.remove(max(ns))
hubo.append(MMM)

ns=list(nums)
Mmm=1
Mmm*=max(ns)
ns.remove(max(ns))
for _ in range(2):
    Mmm*=min(ns)
    ns.remove(min(ns))
hubo.append(Mmm)

if 0 in nums:
    hubo.append(0)


print(max(hubo))