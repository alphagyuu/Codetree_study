import sys

def is_possible(k):
    if k == 0: return True  # 0으로 나누기 방지
    cnt = 0
    for n in ns:
        cnt += n // k
    return cnt >= M

# 입력 속도 향상을 위해 sys.stdin.read 사용 권장
N, M = map(int, sys.stdin.readline().split())
ns = [int(sys.stdin.readline()) for _ in range(N)]

left = 1
right = max(ns) # 모든 전선을 합친 평균보다, 가장 긴 전선의 길이가 현실적인 상한선입니다.
max_k = 0

while left <= right:
    mid = (left + right) // 2
    if mid == 0: # 혹시라도 mid가 0이 되면 다음으로
        left = 1
        continue
        
    if is_possible(mid):
        max_k = mid    # 조건을 만족하면 일단 정답 후보로 저장
        left = mid + 1 # 더 긴 길이가 가능한지 확인하기 위해 오른쪽 탐색
    else:
        right = mid - 1 # 불가능하면 왼쪽(더 짧은 쪽) 탐색

print(max_k)