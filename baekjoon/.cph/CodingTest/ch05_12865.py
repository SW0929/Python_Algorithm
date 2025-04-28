# 문제 4
# 12865
# 재귀(백트래킹)
# 재귀로 정답은 맞으나 시간초과

def recursion(idx, weight, value):
    global answer
    
    if weight > k:
        return
    if idx == n:
        answer = max(answer, value)
        return
    
    recursion(idx+1, weight+items[idx][0], value+items[idx][1])
    
    recursion(idx+1, weight, value)



n, k = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(n)]
answer = 0
recursion(0, 0, 0)