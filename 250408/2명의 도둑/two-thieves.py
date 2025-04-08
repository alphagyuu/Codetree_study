"""
7,1보다
8

2칸씩 순회 -> C안넘치는 제곱의 합을 시작 좌표와 매핑 {(0,0):5 ...} 이런식으로.



N, M, C = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]
# print(grid)
ms = {}
for r in range(N):
    for c in range(N + 1 - M):
        weight = 0
        value = 0
        part = sorted([grid[r][c + i] for i in range(M)], reverse=True)
        for i in range(M):
            if weight + part[i] > C:
                continue
            else:
                weight += part[i]
                value += part[i] ** 2
        # print(grid)
        # print(part)
        # print(weight)
        # print(value)
        ms[(r, c)] = value
mlist = list(ms.items())
mlist.sort(key=lambda item: item[1], reverse=True)
#print(mlist[0:3])
#print(N,M)
out=mlist[0][1]
mlisti=0
while mlist[0][0][0] == mlist[mlisti][0][0] and abs(mlist[0][0][1] - mlist[mlisti][0][1]) < M:
    mlisti+=1
print(mlist[0][1] + mlist[mlisti][1])

"""

# 입력 받기
N, M, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 각 행에서 연속 M개 구간의 최대 가치 계산 배열 (max_profit)
max_profit = [[0] * (N - M + 1) for _ in range(N)]

# 각 구간에 대해 2^M 경우의 수를 전수 조사하여 최대 가치를 구함
for r in range(N):
    for c in range(N - M + 1):
        segment = grid[r][c:c+M]
        best = 0
        # 부분집합 (bitmask) 사용: 0부터 (1<<M)-1까지
        for mask in range(1 << M):
            total_weight = 0
            total_value = 0
            for i in range(M):
                if mask & (1 << i):
                    total_weight += segment[i]
                    total_value += segment[i] ** 2
            if total_weight <= C:
                best = max(best, total_value)
        max_profit[r][c] = best

# 두 구간을 선택할 때 최댓값 계산 (두 도둑의 구간)
ans = 0
for r1 in range(N):
    for c1 in range(N - M + 1):
        # 먼저 하나의 구간 선택
        first_value = max_profit[r1][c1]
        # 두 번째 구간 선택: 같은 행인 경우와 다른 행인 경우 모두 고려
        for r2 in range(r1, N):
            for c2 in range(N - M + 1):
                # 만약 같은 행이라면, 선택한 두 구간이 겹치지 않아야 함
                if r1 == r2 and abs(c1 - c2) < M:
                    continue
                ans = max(ans, first_value + max_profit[r2][c2])
print(ans)
