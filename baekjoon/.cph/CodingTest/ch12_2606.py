# 문제 1
# 2606
# DFS, BFS 둘 다 가능


# DFS 풀이
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

visited = [0 for _ in range(N+1)]

# 그래프 만들기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# DFS
def recur(node):
    visited[node] = 1
    
    for next in graph[node]:
        # 방문했다면 1
        if visited[next] == 1:
            continue
        recur(next)
    
recur(1)

print(sum(visited)-1)

# BFS 풀이
from collections import deque

q = deque()

# 출발 위치
q.append(1)
while len(q) > 0: # q가 0이 된다면 멈출거야
    node = q.popleft() # 1
    visited[node] = 1
    for next in graph[node]:
        if visited[next] == 1:
            continue
        q.append(next)
        
print(sum(visited)-1)
