import sys
input = sys.stdin.readline

n = int(input().rstrip())

numList = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(n):
    print(' '.join(map(str, [i + 1] * n)))