# 문제 1
# 1816
# 완전 탐색으로 품.
N = int(input())
key = [int(input()) for _ in range(N)]

for i in key: # 암호 키 리스트 반복
    for j in range(2, 1000001): # 2 부터 백만 까지 소인수가 있는지 확인
        if i % j == 0: # 소인수가 있다면 NO출력
            print("NO")
            break
        if j == 1000000: # 백만보다 큰 소수이면 YES
            print("YES")