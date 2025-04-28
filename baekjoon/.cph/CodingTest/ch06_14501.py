# 문제 1
# 14501
# 탑다운 DP (메모이제이션)

def recursion(day):
    
    if day == n:
        return 0 # 시작점이 퇴사 당일이라 0을 리턴 해줌
    if day > n:
        return -99999999
    if dp[day] != -1: # 이미 저장되었다면 (재사용)
        return dp[day]
        
    
    # 상담을 한다면
    dp[day] = max(recursion(day+interview[day][0]) + interview[day][1], recursion(day+1))
    return dp[day]
    

n = int(input())

interview = [list(map(int, input().split())) for _ in range(n)]

dp = [-1 for _ in range(n+1)]

recursion(0)
print(max(dp))