# 1090
# ※ 아직 못 풀었음 ※

"""
1. x, y 를 구분해서 계산해준 뒤에 합쳐서
최솟값을 구하면 됨

2. 우리가 한 곳에서 모일 때, 비용을 최소화 하기 위해서는
우리의 집 중 한 곳에서 모이면 된다.

3. 최소 거리를 계산하고 싶다.
그리고 2명이 모여야 한다.
그 점에서 가까운 두명의 거리만 더해주면 되지 않을까
"""
N = int(input())
checker = [list(map(int, input().split())) for _ in range(N)]
checker.sort()

xList = [i[0] for i in checker] # 2차원 리스트 [0] 값 추출
yList = [i[1] for i in checker] # 2차원 리스트 [1] 값 추출

# 각 집의 거리를 확인하기 위한 2차원 배열 생성
answer = [[0 for _ in range(N)] for _ in range(N)]

for i in range(0, N):
    for j in range(0, N):
        if i == j:
            answer[i][j] == 0
        else:
            answer[i][j] += abs(checker[i][0] - checker[j][0]) + abs(checker[i][1] - checker[j][1])

print(answer)
# [[14,15], [15, 14], [15, 16], [16, 15]]
# [14, 15, 15, 16]
# [15, 14, 16, 15]
# [0, 2, 4, 6]