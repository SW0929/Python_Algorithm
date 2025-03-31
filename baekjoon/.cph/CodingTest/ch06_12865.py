# 12865
# 탑다운 DP (메모이제이션)

def recursion(idx, weight):
    
    
    if weight > k:
        return -999999999
    if idx == n:
        return 0
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    
    dp[idx][weight] = max(recursion(idx+1, weight+items[idx][0]) + items[idx][1], recursion(idx+1, weight))
    return dp[idx][weight]
    



n, k = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100_001)] for _ in range(n)]

print(recursion(0, 0))