# 문제 1
# 15649

def recur(number):
    if number == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if i in arr:
            continue
        else:
            arr.append(i)
        recur(number+1)
        arr.pop()
    

N, M = map(int, input().split())
arr = []
recur(0)



# 15650, 15651, 15652, 15654, 15655, 15656 도 풀어야 함.
# 재귀