# 문제 3
# 1407
# 최적화(수학)
"""
A, B = map(int, input().split())

def abcd(N):
    temp_X = N
    for i in range(1, 99):
        temp_X += (N//(2**i)) * ((2**i) - (2**(i-1)))
    return temp_X
print(abcd(B) - abcd(A-1))   
"""

# 2247
def csod(n):
    global ans
    for i in range(2, int(n**0.5) + 1):
        j = n // i
        print(j, i)
        ans += (j + i) * (j - i + 1) // 2 
        ans += (j - i) * i
    return ans
n = int(input())
ans = 0


print(csod(n) % 1000000)