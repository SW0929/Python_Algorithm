# 문제 3
# 19532
# 완전 탐색

a, b, c, d, e, f = map(int, input().split())

# -999 <= x, y <= 999 범위 
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c:
            if d*x + e*y == f:
                print(x, y)
