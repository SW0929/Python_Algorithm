# 문제 1
# 1753
# 다익스트라
# BFS
# 우선순위 큐는 deque를 지원하지 않는다.

from collections import deque
import heapq

N, M = map(int, input().split())

start = int(input())

links = [[] for _ in range(N+1)]
distance = [1e9 for _ in range(N+1)] # 1,000,000,000 # 노드의 값을 업데이트

# 그래프 완성
for _ in range(M):
    A, B, C = map(int, input().split())
    links[A].append([B,C])
    
# BFS
q = []
heapq.heappush(q, [0, start])
distance[start] = 0

while q: # q 배열에 아무것도 없으면 False가 된다.
    # 우선순위 큐를 이용해서, 거리를 보고 정렬할거다
    
    #heapq.heapify(q) # 힙한 상태로 정렬
    #node = q.pop(0) # 힙한 상태가 무너짐
    _w, node = heapq.heappop(q)
    for nxt, weight in links[node]:
        # 1. 각각의 위치에 값을 업데이트
        # 2. 만약에 여러 경로가 있다면 min 비교
        # 3. 시작점으로부터 거리를 봐서, 짧은 순서대로 탐색 (오염 발생하기 때문)
        if distance[node] + weight < distance[nxt]:
            distance[nxt] = distance[node] + weight
            #q.append([distance[nxt], nxt]) # 거리값, 인덱스값
            heapq.heappush(q, [distance[nxt], nxt]) # q에 거리값, 인덱스값 넣기
        
print(distance)


"""
# 최소값을 찾는 함수인데 우선순위 큐로 대체가능
def shortest_finder():
    mini = 1e9
    idx = 0
    for i in range(1, N+1):
        if distance[i] <= mini:
            idx = i
            mini = distance[i]
    return idx

while q: # q 배열에 아무것도 없으면 False가 된다.
    node = q.popleft()
    for nxt, weight in links[node]:
        # 1. 각각의 위치에 값을 업데이트
        # 2. 만약에 여러 경로가 있다면 min 비교
        # 3. 시작점으로부터 거리를 봐서, 짧은 순서대로 탐색 (오염 발생하기 때문)
        distance[nxt] = min(distance[node] + weight, distance[nxt])
        q.append(nxt)
        visited[nxt] = 1
        
        idx = shortest_finder()
        
        if idx in q:
            q.remove(idx)
            q.appendleft(idx)"""