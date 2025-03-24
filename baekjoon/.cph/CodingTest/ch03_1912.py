# 1912
# 다이나믹 프로그래밍 ( 메모이제이션 )
# 누적합


n = int(input())

# 수열 입력
nList = list(map(int, input().split()))

# n 보다 1 큰 누적합 공간 만들기
prefix= [0 for _ in range(n+1)]

"""
누적합을 구하는데 연속된 자리 수 합이 수열 한 자리 수
보다 작을 경우 한 자리 수를 입력 한다.
"""
for i in range(n):
    prefix[i+1] = max(prefix[i] + nList[i], nList[i])

# 수열의 크기 보다 1 크게 만들었기 때문에 맨 앞 인덱스 제외
print(max(prefix[1:]))