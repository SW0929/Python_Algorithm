# 2805
# 이분탐색

N, M = map(int, input().split())
forest = list(map(int, input().split()))

s = 1
e = max(forest)

while s <= e:
    mid = (s+e) // 2
    wood = 0
    for tree in forest:
        if tree >= mid:
            wood += tree - mid
    if wood >= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)    
    
""" 
# 시간 초과 해결
import sys

# 입력 최적화
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
forest = list(map(int, input().split()))

# 이분 탐색
s, e = 0, max(forest)

while s <= e:
    mid = (s + e) // 2
    wood = sum(tree - mid for tree in forest if tree > mid)  # 나무 길이 계산 최적화

    if wood >= M:
        s = mid + 1  # 더 높이 자를 수 있음
    else:
        e = mid - 1  # 높이를 낮춰야 M만큼 얻을 수 있음

# 최적의 높이 출력
print(e)
"""