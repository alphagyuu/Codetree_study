N,M,P = map(int,input().split())
messages=[
    list(map(str,input().split()))
    for _ in range(M)
]
messages=[[c,int(p)] for c,p in messages]
#print(messages)

#[의심] = [A~...] N명
#messages[P-1] 부터 문자 보냈으면 -> [의심]에서 제거
#읽은사람수는...?
# -> D=0 에서 E가 제외되는 이유!
# 안읽은사람이 없잖아!!
# 또다른경우는..?
# 인원수 변화가 없는 경우: 계속 동일한 멤버로 채팅했음. (왜냐면 나갔다 들어오는게 불가능하니까.)

suspects=[chr(x+ord('A')) for x in range(N)]
#suspects.remove('A')
#print(suspects)

for i in range(M-1,P-2,-1):
    if messages[i][0] in suspects:
        suspects.remove(messages[i][0])

peop_in_time_p=messages[P-1][1]

for i in range(P-2,-1,-1):
    if messages[i][1]==peop_in_time_p and messages[i][0] in suspects:
        suspects.remove(messages[i][0])

if messages[P-1][1]==0:
    print("")
else:
    print(*suspects)
