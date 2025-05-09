# 문제 3
# 14501
# 재귀(백트래킹)
import sys
input = sys.stdin.readline

def recursion(day, price):
    global result
    if day == n-1:
        result = max(result, price)
        return
    if day > n - 1:
        return
    
    # 상담을 한다면
    recursion(day+interview[day][0], price+interview[day][1])

    # 상담을 하지 않는다면
    recursion(day+1, price)

n = int(input())

interview = [list(map(int, input().split())) for _ in range(n)]
result = 0
recursion(0, 0)
print(result)