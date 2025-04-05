# 문제 2
# 1978
# 정수론(수학)
"""
N = int(input())
num = list(map(int, input().split()))
answer = 0
for i in num:
    check = 0
    if i == 1:
        continue
    
    for j in range(2,int(i**0.5)+1):
        
        if i % j == 0:
            check += 1
            
    if check == 0:
        answer += 1
        
print(answer)
"""

# 11653
# 소인수 분해
"""
N = int(input())
i = 2

while i * i <= N: # 소인 수 중 가장 큰 수는 루트N 보다 작다.
    
    if N % i == 0:
        print(i)
        N = N // i
    else:
        i += 1
# 큰 소수 일 경우를 대비
if N > 1:
    print(N)
"""
# 14232
# 소인수 분해 문제
# 문제 잘 보고 판단하기!!!
N = int(input())
i = 2
result = []
while i * i <= N:
    if N % i == 0:
        result.append(i)
        N = N // i
    else:
        i += 1
if N > 1:
    result.append(N)

print(len(result))
print(*result)