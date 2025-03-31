# 14501
# 바텀업 DP(점화식)

n = int(input())

interview = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for day in range(n)[::-1]:
    
    if day + interview[day][0] > n:
        dp[day] = dp[day+1]
    else:
        dp[day] = max(dp[day+interview[day][0]] + interview[day][1], dp[day+1])

print(max(dp))