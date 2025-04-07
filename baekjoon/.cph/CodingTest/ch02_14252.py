# 문제 5
# 14252
# 정수론(공약수)
"""
for i in range(42, 2184):
    if gcd(42, i) == 1:
        if gcd(2184, i):
            count += 1
            break
        
for j in range(2184, 2200):
    if gcd(2184, j) == 1:
        if gcd(2199, j) == 1:
            count += 1
            break
    if j == 2199:
        count += 2
"""
# 이거는 왤케 어렵냐 -> ㅈ밥

import math
n = int(input())
a = sorted(list(map(int, input().split())))
count = 0

for i in range(len(a) - 1):
    if math.gcd(a[i], a[i+1]) == 1:
        continue
    for j in range(a[i], a[i+1]):
        if math.gcd(a[i], j) == 1:
            if math.gcd(a[i+1], j) == 1:
                count += 1
                break
        if j == a[i+1] - 1:
            count += 2
print(count)