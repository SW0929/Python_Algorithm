import sys
input = sys.stdin.readline

T = int(input())

infor = {
    '0': '1111110',
    '1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
    '6': '1011111',
    '7': '1110010',
    '8': '1111111',
    '9': '1111011',
    ' ': '0000000'
}


for _ in range(T):
    a, b = map(str, input().rstrip().split())
    
    a = a.rjust(5) # 5개 공간 확보하고 없으면 빈칸으로 채움
    b = b.rjust(5)
    
    result = 0
    for i in range(5):
        for j in range(7):
            if (infor[a[i]][j] != infor[b[i]][j]):
                result += 1

    
    print(result)
    