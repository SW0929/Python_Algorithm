"""
# 2178
# BFS
import sys
from collections import deque
input = sys.stdin.readline

def bfs(sy, sx):
    
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 1
    
    while q:
        y, x = q.popleft()
        for ey, ex in [[1,0], [-1,0], [0,1], [0,-1]]:
            ny, nx = y+ey, x+ex
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and miro[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    

N, M = map(int, input().strip().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
miro = [list(map(int, input().strip())) for _ in range(N)]

bfs(0,0)

print(visited[N-1][M-1])
"""
# 1697
# BFS

import sys
from collections import deque
input = sys.stdin.readline

X, K = map(int, input().strip().split())

visited = [0] * 100_001

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        current = q.popleft()
        if current == K:
            return visited[current]
        for next in [current - 1, current + 1, current * 2]:
            if 0 <= next < 100_001 and visited[next] == 0:
                visited[next] = visited[current] + 1
                q.append(next)
            
        print(visited[:17])
print(bfs(X))