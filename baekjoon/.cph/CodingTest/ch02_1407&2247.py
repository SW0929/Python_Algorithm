# 문제 3
# 1407
# 최적화(수학)

A, B = map(int, input().split())

def abcd(N):
    temp_X = N
    for i in range(1, 99):
        temp_X += (N//(2**i)) * ((2**i) - (2**(i-1)))
    return temp_X
print(abcd(B) - abcd(A-1))    

# 2247