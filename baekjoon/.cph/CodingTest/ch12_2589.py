# 2589
# BFD 그래프 탐색 문제
# 시간 초과

from collections import deque

Y, X = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(Y)]

maxi = 0

for y in range(Y):
    for x in range(X):
        if graph[y][x] == "L":
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            distance = [[0 for _ in range(X)] for _ in range(Y)]
            
            # BFS
            q = deque()
            q.append([y, x]) # 시작점
            visited[y][x] = 1 # 첫번째 시작점 방문처리
            while q:
                ey, ex = q.popleft()
                
                # 4방향 탐색
                for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ny, nx = ey+dy, ex+dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if graph[ny][nx] == "L":
                            if visited[ny][nx] == 0: # 방문한적이 없냐
                                visited[ny][nx] = 1
                                distance[ny][nx] = distance[ey][ex] + 1
                                maxi = max(maxi, distance[ny][nx])
                                q.append([ny, nx])
                                
print(maxi)