# 문제 2
# 1978
# 정수론(수학)
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

# 11653

# 14232