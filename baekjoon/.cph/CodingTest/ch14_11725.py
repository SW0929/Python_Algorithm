# 11725
# 트리
import sys
sys.setrecursionlimit(10**6)
N = int(input())

graph = [[] for _ in range(N+1)]

par = [0 for _ in range(N+1)]

# 만약 자식의 수를 알고 싶으면
child = [0 for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split())
    
    # 양방향
    graph[a].append(b)
    graph[b].append(a)
    
    result = [[] for _ in range(3)]
def recur(node,prv):
    
    par[node] = prv

    for nxt in graph[node]:
        if nxt == prv: # 역주행 방지
            continue
        recur(nxt,node)
    child[prv] += 1 # 자식의 수 증가
     

recur(1, 0)
print(*par[2:], sep="\n")