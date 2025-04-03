# 문제 5
# 14252
# 정수론(공약수)

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