# 3273
# 투포인터

n = int(input())

arr = sorted(list(map(int, input().split())))

x = int(input())

front = 0
back = n - 1

count = 0

while front < back:
    if arr[front] + arr[back] == x:
        count += 1
    if arr[front] + arr[back] > x:
        back -= 1
    else:
        front += 1
        
print(count)