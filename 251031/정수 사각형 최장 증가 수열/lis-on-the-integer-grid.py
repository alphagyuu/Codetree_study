import sys
# Python의 재귀 깊이 제한을 늘려줍니다 (N이 클 경우 필요)
sys.setrecursionlimit(1000000) 

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
    
# dp 배열을 0으로 초기화합니다. (0: 아직 계산되지 않음)
dp = [[0]*n for _ in range(n)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def in_grid(r,c):
    return 0<=r<n and 0<=c<n

def dfs(r, c):
    # 1. 🛑 메모이제이션 (기저 사례): 이미 계산된 값이라면 바로 반환
    if dp[r][c] > 0:
        return dp[r][c]
    
    # 2. 초기값 설정: 현재 위치에서 시작하는 경로는 최소 길이 1
    max_len_from_neighbors = 0
    
    # 3. 🔍 4방향 탐색 (재귀 호출)
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        
        # 핵심 조건: 그리드 내부에 있고, 값이 더 커야 함
        if in_grid(nr, nc) and grid[nr][nc] > grid[r][c]:
            # 이웃 칸의 최장 경로 길이를 재귀적으로 가져와 최댓값 갱신
            current_len = dfs(nr, nc)
            max_len_from_neighbors = max(max_len_from_neighbors, current_len)
            
    # 4. 💾 DP 값 저장: 이웃 최댓값 + 1 (현재 칸)
    dp[r][c] = 1 + max_len_from_neighbors
    return dp[r][c]

# --- 메인 실행 ---

# 모든 칸을 시작점으로 삼아 최장 경로 계산을 시작합니다.
for r in range(n):
    for c in range(n):
        dfs(r, c)

# 최종 답은 계산된 dp 값들 중 가장 큰 값입니다.
ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, dp[r][c])

print(ans)