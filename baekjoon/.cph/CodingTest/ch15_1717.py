# 1717
# 유니온 파인드
# union/find 최적화는 하나만 하면 됨
# 파이썬을 코테를 친다면 유니온이 성능이 더 좋기 때문에 유니온 쓰는게 유리
# 최적화에 문제가 있음 확인바람
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def _union(A, B): # 최대 높이를 확인해서 합쳐준다
    
    A = _find(A)
    B = _find(B)
    if A == B:
        return
    
    if rank[A] < rank[B]:
        par[A] = B
    elif rank[B] < rank[A]:
        par[B] = A
    else:
        par[A] = B # 반대로 해도 상관없음
        par[B] += 1
    
    
def _find(A):
    if par[A] != A: # 만약에 스스로를 부모로 칭하고 있다면
        par[A] = _find(par[A])  # 부모를 루트로 직접 설정 (경로 압축)
    return par[A]

    """# 최적화 코드
    if par[A] == A: # 만약에 스스로를 부모로 칭하고 있다면
        return A
    else:
        par[A] = _find(par[A])
        return _find(par[A])"""
    
    
    
    
    

N, M = map(int, input().split())

rank = [0 for _ in range(N+1)] # 노드, 

answer = []
par = [i for i in range(N+1)]
# [0, 1, 2, 3, 4, 5, 6, 7]

for _ in range(M):
    X,A,B = map(int, input().split())
    
    if X == 0:
        _union(A, B)
    else:
        if _find(A) == _find(B):
            #answer.append("YES")
            print("YES")
        else:
            #answer.append("NO")
            print("NO")
            
#print(*answer, sep="\n")