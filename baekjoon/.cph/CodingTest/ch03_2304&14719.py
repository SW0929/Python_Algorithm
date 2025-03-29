# 2304 & 14719
# 완전 탐색 | 누적합 | 투포인터 로 풀 수 있음

N = int(input())
warehouse = [list(map(int, input().split())) for _ in range(N)]


warehouse.sort(key=lambda x:x[1])
big_col = warehouse[-1][1] # 기둥 높이가 가장 큰 값
big_row = warehouse[-1][0] # 기둥 위치

print(big_row, big_col)
warehouse.sort()

brick = 0
 
height = warehouse[0][0] # 초기 값 위치
for i in range(height, big_row):
    


print(brick)