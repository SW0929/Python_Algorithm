# 문제 1
# 10815
# 이분탐색

N = int(input())

arr1 = sorted(list(map(int, input().split())))

M = int(input())

arr2 = list(map(int, input().split()))

for number in arr2:
    s = 0
    e = N-1
    
    flag = False
    while s <= e: # 교차 된다면 종료
        mid = (s+e) // 2
        if number == arr1[mid]:
            flag = True
            break
        elif number < arr1[mid]: # 다운
            e = mid - 1
        else: # 업
            s = mid + 1
    if flag:
        print(1, end=" ")
    else:
        print(0, end=" ")