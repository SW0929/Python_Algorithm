# 문제 2
# 2503
# 재귀함수로 풀이

import sys

sys.setrecursionlimit(99999999)

def checker(idx,number):
    _number = hint[idx][0]
    _strike = hint[idx][1]
    _ball = hint[idx][2]

    strike = 0
    ball = 0

    _A = _number // 100
    _B = (_number - (_A * 100)) // 10 
    _C = _number % 10


    A = number // 100
    B = (number - (A * 100)) // 10 
    C = number % 10 

    if A == 0 or B == 0 or C == 0:
        return False

    if A == B or A == C or B == C:
        return False

    if A == _A:
        strike+= 1
    if B == _B:
        strike+= 1
    if C == _C:
        strike+= 1
    
    if A == _B or A == _C:
        ball += 1
    if B == _A or B == _C:
        ball += 1
    if C == _A or C == _B:
        ball += 1
    
    if strike == _strike and ball == _ball:
        return True

    return False


def recur(hint_idx, number):
    global answer
    if hint_idx == N:
        answer += 1
        recur(0, number+1)
        return
    if number == 1000:
        return
    
    # 만약 힌트에 통과했다면
    # 스트라이크 카운트랑 볼 카운특가 동일하다면
    if checker(hint_idx,number):
        recur(hint_idx+1, number)
    
    # 만약 힌트에 통과하지 못했다면
    else:
        recur(0, number+1)


N = int(input())

hint = [list(map(int, input().split())) for _ in range(N)]

answer = 0
recur(0, 100)
print(answer)