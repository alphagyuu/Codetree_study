'''
1 3 9 7 5 11 3
1 3/ 9/ 7 5/ 11/ !3

짝 개수 >= 홀 개수. -> 가능.

홀수 개수: 7
짝 2 홀 3 불가능.
짝 3 홀 1으로 가능. -> 3개 (1*2 +1)

만약
짝2 홀2 -> 4개
'''

N=int(input())
nums=list(map(int,input().split()))
bits=[n%2 for n in nums]
#print(bits)

evens=bits.count(0)
odds=bits.count(1)
#print(evens,odds)

while evens<odds:
    odds-=2
    evens+=1
#print(evens,odds)

if evens>odds:
    print(odds*2+1)
else:
    print(odds*2)