# 2961
# 재귀(백트래킹)

def recursion(idx, sour, bitter, use):
    global answer
    if idx == n:
        if use == 0:
            return
        else:
            result = abs(sour - bitter)
            answer = min(answer, result)
        return
    # 재료를 사용했을 경우
    recursion(idx+1, ingredient[idx][0]*sour, ingredient[idx][1]+bitter, use+1)
    
    # 재료를 사용하지 않았을 경우
    recursion(idx+1, sour, bitter, use)


n = int(input())

answer = 9999999999

ingredient = [list(map(int, input().split())) for _ in range(n)]

recursion(0, 1, 0, 0)
print(answer)