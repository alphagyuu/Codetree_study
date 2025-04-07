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

suspects=[chr(x+ord('A')) for x in range(N)]
#suspects.remove('A')
#print(suspects)


for i in range(P-1,M):
    if messages[i][0] in suspects:
        suspects.remove(messages[i][0])

print(*suspects)
