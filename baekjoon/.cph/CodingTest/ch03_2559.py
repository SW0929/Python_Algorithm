# 문제 1
# 2559
# 누적합

N, K = map(int, input().split()) # 전체 날짜의 수, 간격
tem = list(map(int, input().split())) # 매일 측정한 온도

prefix = [ 0 for _ in range(N+1)] # 누적합 리스트 초기화

for i in range(N):
    prefix[i+1] = prefix[i] + tem[i] # 누적합

result = [] # 간격 만큼의 합을 구하기 위한 리스트 생성
for i in range(K, N+1): # 간격 k 부터 시작
    # 간격 인덱스 부터 1 증가 - (간격 인덱스-간격)
    result.append(prefix[i] - prefix[i - K])
print(max(result))

"""
print("누적합 : ", prefix)
print("결과 : ", result)
"""