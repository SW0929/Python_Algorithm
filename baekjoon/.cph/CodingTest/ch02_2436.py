# 문제 4
# 2436
# 최적화
# GCD(최대공약수)

import math
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