# 1520
# 2차원 DP
import sys
sys.setrecursionlimit(10**6)

def recur(y, x):
    
    if y == Y-1 and x == X-1:
        return 1
    
    # dp 재사용, 0으로 하면 탐색하지 않은 (0, 0) 이 계속 재귀를 타게 됨.
    if dp[y][x] != -1:
        return dp[y][x]
    
    
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        # 좌표 이동
        ey = y + dy
        ex = x + dx
        # 주어진 표를 벗어나지 못하게 예외처리
        if 0 <= ey < Y and 0 <= ex < X:
            # 조건 : 현재 값보다 큰 곳으로 이동 가능
            if graph[y][x] > graph[ey][ex]:
                 
                dp[y][x] += recur(ey, ex)
                
    return dp[y][x]



Y, X = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(Y)]

dp = [[-1 for _ in range(X)] for _ in range(Y)]

print(recur(0, 0))