# 문제 1
# 1937
# 2차원 DP

# runtimeError 가 발생하면 재귀 범위를 늘려주자
import sys
sys.setrecursionlimit(10**6)

def recur(y, x):
    # dp 재사용
    if dp[y][x] != 1:
        return dp[y][x]
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        # 좌표 이동
        ey = y + dy
        ex = x + dx
        # 주어진 표를 벗어나지 못하게 예외처리
        if 0 <= ey < n and 0 <= ex < n:
            # 조건 : 현재 값보다 큰 곳으로 이동 가능
            if graph[y][x] < graph[ey][ex]:
                 
                dp[y][x] = max(dp[y][x], recur(ey, ex) + 1) # 내가 이동하고 돌아올 때 1을 가져온다
    return dp[y][x]



n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[1 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        point = recur(y, x)
        
print(max(map(max, dp)))
        