# 11660
# 2차원 누적합
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
findSum = [list(map(int, input().split())) for _ in range(M)]

prefix = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 누적합 계산
for x in range(N):
    for y in range(N):
        prefix[x+1][y+1] = prefix[x+1][y] + prefix[x][y+1] - prefix[x][y] + graph[x][y]

# 계산한 누적합에서 값을 도출
for i in findSum:
    answer = prefix[i[2]][i[3]] - prefix[i[0]-1][i[3]] - prefix[i[2]][i[1]-1] + prefix[i[0]-1][i[1]-1]
    print(answer)    