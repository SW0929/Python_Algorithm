# 문제 2
# 14568
# 완전탐색으로 문제 품.

N = int(input())

result = 0
# 각 인원이 받을 수 있는 사탕의 갯수는 최소 0개, 최대 N개
for A in range(0, N+1):
    for B in range(0, N+1):
        for C in range(0, N+1):
            # 조건 1 : 남는 사탕은 없어야 한다.
            if A + B + C == N:
                # 조건 2 : 남규는 영훈이보다 2개 이상 많은 사탕을 가져야 한다.
                if A >= B+2:
                    # 조건 3 : 셋 중 사탕을 0개 받는 사람은 없어야 한다.
                    if A != 0 and B != 0 and C != 0:
                        # 조건 4 : 택희가 받는 사탕의 수는 홀수개가 되어서는 안 된다.
                        if C % 2 == 0:
                            result += 1
print(result)                            