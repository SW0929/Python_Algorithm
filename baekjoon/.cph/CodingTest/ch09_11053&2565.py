# 11053
# LIS

A = int(input())

subsequence = list(map(int, input().split()))

dp = [1 for _ in range(A)]

for i in range(A):
    for j in range(i):
        if subsequence[i] > subsequence[j]:
            dp[i] = max(dp[i], dp[j]+1)
    
print(max(dp))





















#2565