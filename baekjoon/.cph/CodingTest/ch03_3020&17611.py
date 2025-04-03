# 문제 5
# 3020
# 누적합

N, M = map(int, input().split())

# nList = [int(input()) for _ in range(N)] # 석순/종유석 길이 표시

crack = [0] * M

# 충돌 횟수 맨 앞/뒤 체크
for a in range(N):
    i = int(input())
    if a % 2 == 0:
        crack[0] += 1
        crack[i] -= 1
    else:
        crack[M - i] += 1

# 누적합
for i in range(1, M):
    crack[i] += crack[i-1]

result = min(crack)
frequency = crack.count(min(crack))
print(result, frequency)



# 17611