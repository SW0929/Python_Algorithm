# 1149
# 바텀업 DP
# 코드 다시 보기

n = int(input())

price_color = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(3) for _ in range(n)]

for k in range(3):
    dp[0][k] = price_color[0][k]

for idx in range(1, n):
    for RGB in range(3):
        if RGB == 0:
            dp[idx][RGB] = min(dp[idx-1][1], dp[idx-1][2]) + price_color[idx][RGB]
        if RGB == 1:
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][2]) + price_color[idx][RGB]
        if RGB == 2:
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][1]) + price_color[idx][RGB]
    for f in range(3):
        dp[0][f] = dp[1][f]

print(min(dp[-1]))