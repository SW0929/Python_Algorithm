# 문제 2
# 12865
# 바텀업 DP (점화식)

n, k = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for y in range(1, n+1):
    
    for x in range(k+1):
        weight, value = items[y-1] # 입력 배열과 dp 인덱스를 맞추기 위해 y-1 사용
        if x < weight:
            dp[y][x] = dp[y - 1][x]
        else:
            dp[y][x] = max(dp[y-1][x-weight] + value, dp[y-1][x])

print(dp)