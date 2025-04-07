# 문제 3
# 2304
# 완전 탐색 | 누적합 | 투포인터 로 풀 수 있음
"""
N = int(input())
column = [list(map(int, input().split())) for _ in range(N)]

column.sort()
result = 0
max_height = 0
max_index = 0
# 가장 높은 기둥 크기, 인덱스 구함
for i in range(N):
    if column[i][1] > max_height:
        max_height = column[i][1]
        max_index = i
        
check_col = column[0][1]
check_row = column[0][0]
# 완쪽부터 최대 기둥까지
for i in range(1, max_index+1):
    result += check_col * (column[i][0] - check_row)
    print(result)
    if check_col < column[i][1]:
        check_col = column[i][1]
    
    check_row = column[i][0]


check_col = column[-1][1]
check_row = column[-1][0]
# 오른쪽부터 최대 기둥까지
for i in range(N-2, max_index-1,-1):
    result += check_col * (check_row - column[i][0])
    print(result)
    if check_col < column[i][1]:
        check_col = column[i][1]
        
    check_row = column[i][0]
    
print(result+max_height)
"""

# 14719
h, w = map(int, input().split())
colums = list(map(int, input().split()))

max_colum = 0
max_index = 0
result = 0
# 기둥 최대 값, 인덱스
for i in range(w):
    if colums[i] > max_colum:
        max_colum = colums[i]
        max_index = i
        


if colums.count(0) != w-1:
    check_col = colums[0]
    for i in range(1, max_index):
        if check_col > colums[i]:
            result += check_col - colums[i]
        else:
            check_col = colums[i]
            
    if max_index != w - 1:
        check_col = colums[-1]
        for i in range(w-2, max_index, -1):
            if check_col > colums[i]:
                result += check_col - colums[i]
            else:
                check_col = colums[i]
print(result)