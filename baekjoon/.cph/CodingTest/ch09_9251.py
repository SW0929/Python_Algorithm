# 문제 2
# 9251
# LCS, 아이디어가 중요한 문제
# 문제 푸는 방식을 이해하면 됨.

M = list(str(input()))
N = list(str(input()))

dp = [[0 for _ in range(len(N)+1)] for _ in range(len(M)+1)]

for i in range(1, len(M) + 1):
    for j in range(1, len(N) + 1):
        if M[i-1] == N[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[len(M)][len(N)])