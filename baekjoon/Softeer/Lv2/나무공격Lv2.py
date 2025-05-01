
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [list(map(int, input().rstrip().split())) for _ in range(n)]
attack = [list(map(int, input().rstrip().split())) for _ in range(2)]

bad = [0] * n
for i in range(n):
    bad[i] = tree[i].count(1)

for i in range(2):
    for j in range(attack[i][0]-1, attack[i][1]):
        
        if bad[j] == 0:
            continue
        else:
            bad[j] -= 1
        

print(sum(bad))