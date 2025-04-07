N, H = map(int, input().split())
prefix = [0] * H

for i in range(N):
    a = int(input())
    if i % 2 == 0:
        prefix[0] += 1
        prefix[a] -= 1
    else:
        prefix[H-i] += 1
for i in range(1, H):
    prefix[i] += prefix[i-1]

result = min(prefix)
fre = prefix.count(result)
print(result, fre)