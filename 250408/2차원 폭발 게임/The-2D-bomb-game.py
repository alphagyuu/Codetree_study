def printarr(arr):
    for row in arr:
        print(*row)
    return 0

def count_non_zeros(arr):
    cnt=0
    for row in arr:
        for i in row:
            if i>0:
                cnt+=1
    print(cnt)
    return 0

def can_boom(): # 무한루프..? -> 0도 콤보로 처리중
    for c in range(N):
        before=0
        start_i=0
        combo=0
        for r in range(N):
            if box[r][c]==0:
                combo=0
                before=0
            elif before!=box[r][c]:
                # M콤보 이상 제거.
                if combo>=M and before!=0:
                    return True
                before = box[r][c]
                start_i = r
                combo=1
            else:
                combo+=1

        if combo>=M and before!=0:
            return True
    return False

def boom():
    for c in range(N):
        before=0
        start_i=0
        combo=0
        for r in range(N):
            if box[r][c]==0:
                combo=0
                before=0
            elif before!=box[r][c]:
                # M콤보 이상 제거.
                if combo>=M and before!=0:
                    for i in range(combo):
                        box[i+start_i][c]=0
                before = box[r][c]
                start_i = r
                combo=1
            else:
                combo+=1
        if combo>=M and before!=0:
            for i in range(combo):
                box[i+start_i][c]=0 #콤보가 종료까지 이어지는 경우 처리
    return 0

def gravity():
    cols=[[] for _ in range(N)]
    for c in range(N):
        for r in range(N):
            cols[c].append(box[r][c])
    for col in cols:
        while 0 in col:
            col.remove(0)
    for c in range(len(cols)):
        cols[c]=[0]*(N-len(cols[c]))+cols[c]
    for c in range(N):
        for r in range(N):
            box[r][c]=cols[c][r]
    return 0

"""
0,0 0,1 0,2
1,0
2,0
i,j

2,0 1,0 0,0
j, 2-i
0,0 0,1 0,2

"""

def rotate():
    newarr=[[0]*N for _ in range(N)]
    global box
    for r in range(N):
        for c in range(N):
            newarr[c][N-1-r]=box[r][c]
    box=newarr



N,M,K=map(int,input().split())
box=[
    list(map(int,input().split()))
    for _ in range(N)
]
#print(N,M,K)
for _ in range(K):
    while can_boom():
        boom()
        gravity()
    rotate()
    gravity()
while can_boom():
    boom()
    gravity()
    #print(".")
#printarr(box)
count_non_zeros(box)