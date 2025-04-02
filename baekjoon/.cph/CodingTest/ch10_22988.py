# 22988
# 투포인터

N, X = map(int, input().split())

arr = sorted(list(map(int, input().split())))

count = 0

remain = 0

s = 0
e = N-1

# 조건 잘 생각해서 풀기

while s <= e: # 교차될 때 종료
    # 원하는 용량에 적확히 맞으면 바로 추가해준다.
    if arr[e] == X:
        count += 1
        e -= 1
        continue
    # 인덱스가 만나면 자투리 하나 추가
    if s == e:
        remain += 1
        break
    
    if arr[s] + arr[e] >= X/2 :
        count += 1
        s += 1
        e -= 1
    else: # 두 수를 더했을 때 X/2 값을 넘지 못하면 작은 수는 자투리로 넘겨준다.
        s += 1
        remain += 1
        
print(count + remain//3)