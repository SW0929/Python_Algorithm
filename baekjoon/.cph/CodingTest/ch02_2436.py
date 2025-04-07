# 문제 4
# 2436
# 최적화
# GCD(최대공약수)


"""
math.gcd() # 최대공약수
math.lcm() # 최대공배수

# 최대공약수
def _gcd(a, b):
    while a % b != 0: # 나머지가 0이 되는 순간 멈춘다.
        tmp = a%b
        a = b
        b = tmp
    return b

# 최대공배수
def _lcm(a, b):
    return a*b//_gcd(a,b)
"""
import math
a, b = map(int ,input().split())

_gcd = math.gcd(a, b)
_lcm = math.lcm(a, b)
gcd_lcm = _gcd * _lcm
result = float('inf')
res = (0, 0)

for i in range(1, int(gcd_lcm ** 0.5)+1):
    if gcd_lcm % i == 0:
        x = i
        y = gcd_lcm//i
        if math.gcd(x, y) == a and math.lcm(x, y) == b:
            if x+y < result:
                res = (x, y)

print(res[0], res[1])