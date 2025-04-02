# 1991
# 트리

N = int(input())

graph = [[] for _ in range(130)]

for _ in range(N):
    a,b,c = map(str, input().split())
    # 아스키코드
    a = ord(a)
    b = ord(b)
    c = ord(c)
    
    graph[a].append(b)
    graph[a].append(c)
    
result = [[] for _ in range(3)]

def recur(node):
    # 아무것도 없는 경우 리턴
    if node == 46:
        return
        
    # print(chr(node), end=" ")
        
    # for nxt in graph[node]:
        #recur(nxt)
            
    # print(chr(node), end=" ")
        
    result[0].append(chr(node)) # 전위
    recur(graph[node][0])
    result[1].append(chr(node))  # 중위
    recur(graph[node][1])
    result[2].append(chr(node))  # 후위
recur(65)

print("".join(result[0]))
print("".join(result[1]))
print("".join(result[2]))