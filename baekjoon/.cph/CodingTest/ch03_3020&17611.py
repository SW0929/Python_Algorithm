# 문제 5
# 3020
# 누적합
"""
N, M = map(int, input().split())

# nList = [int(input()) for _ in range(N)] # 석순/종유석 길이 표시

crack = [0] * M

# 충돌 횟수 맨 앞/뒤 체크
for a in range(N):
    i = int(input())
    if a % 2 == 0: # 석순
        crack[0] += 1
        crack[i] -= 1
    else: # 종유석
        crack[M - i] += 1

# 누적합
for i in range(1, M):
    crack[i] += crack[i-1]

result = min(crack)
frequency = crack.count(min(crack))
print(result, frequency)
"""


# 17611
# 모르겠음

n = int(input())
x = []
y = []
for i in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
max_x = 0
max_y = 0
if min(x) == 0:
    max_x = max(x) + 1
else:
    max_x = max(x) - min(x)
if min(y) == 0:
    max_y = max(y) + 1
else:
    max_y = max(y) - min(y)

print(max(max_x, max_y))