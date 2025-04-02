# 1197
# 최소 스패닝 트리

# 프림
import heapq
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # 노드의 개수 + 1
visited = [0 for _ in range(N+1)]

# 1번부터 3번까지 노드가 주어지니
# 0 1 2 3 연결 관계를 표현하기 위해 만듬

for _ in range(M):
    A, B, C = map(int, input().split())
    
    # 양방향 연결
    graph[A].append([C,B])
    graph[B].append([C,A])



# 다익스트라
count = 0
answer = 0

q = [[0,1]] # 1에서 출발할거다 가중치 없이

while q: # q가 아무것도 없어질 때까지
    if count == N:
        break
    
    weight, node = heapq.heappop(q) # 최소비용을 꺼내준다.
    
    if visited[node] == 0:
        visited[node] = 1
        answer += weight
        count += 1
        
        for nxt in graph[node]:
            heapq.heappush(q, nxt)

print(answer)