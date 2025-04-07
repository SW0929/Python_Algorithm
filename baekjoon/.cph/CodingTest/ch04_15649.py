# 문제 1
"""
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
"""

# 재귀

# 15650
"""
def recur(number):
    if number == M:
        c = sorted(arr.copy())
        if c not in result:
            result.append(c)
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
result = []
recur(0)

for i in result:
    print(*i)
"""

# 15651
"""
def recur(number):
    if number == M:
        print(*arr)
        return
    for i in range(1, N+1):
        arr.append(i)
        recur(number+1)
        arr.pop()

N, M = map(int, input().split())
arr = []
recur(0)
"""

# 15652
"""
def recur(number, start):
    
    if number == m:
        print(*arr)
        return
    for i in range(start, n+1):
        arr.append(i)
        recur(number+1, i)
        arr.pop()
        
n, m = map(int, input().split())
arr = []
recur(0, 1)
"""

# 15654
"""
def recur(number, nums):
    if number == M:
        print(*arr)
        return
    for i in nums:
        if i in arr:
            continue
        else:
            arr.append(i)
        recur(number+1, nums)
        arr.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []
recur(0, nums)
"""

# 15655
"""
def recur(number, nums):
    if number == M:
        result.add(tuple(sorted(arr)))
        return
    for i in nums:
        if i in arr:
            continue
        else:
            arr.append(i)
        recur(number+1, nums)
        arr.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []
result = set()
recur(0, nums)
for i in sorted(result):
    print(*i)
"""

# 15656
"""
def recur(number, nums):
    if number == M:
        print(*arr)
        return
    for i in nums:
        arr.append(i)
        recur(number+1, nums)
        arr.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []
recur(0, nums)
"""