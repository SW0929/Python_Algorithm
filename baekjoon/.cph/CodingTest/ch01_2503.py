# 2503
# 완전탐색

N = int(input()) # 질문 횟수
hint = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            cnt = 0
            if a == b or b== c or c == a:
                continue
            for arr in hint:
                strikeCount = 0
                ballCount = 0

                number = list(map(int, str(arr[0]))) # 힌트 세 자리 숫자 한자리 씩 나눔
                strike = arr[1]
                ball = arr[2]
                
                # 스트라이크 확인
                if a == number[0]:
                    strikeCount += 1
                if b == number[1]:
                    strikeCount += 1
                if c == number[2]:
                    strikeCount += 1
                
                # 볼 체크할 때
                # 이미 스트라이크 된 숫자 포함 주의
                if a in number and a != number[0]:
                    ballCount += 1
                if b in number and b != number[1]:
                    ballCount += 1
                if c in number and c != number[2]:
                    ballCount += 1
                # 힌트와 같으먼 cnt 증가
                if ball == ballCount and strike == strikeCount:
                    cnt += 1
                
            if cnt == N:
                answer += 1
print(answer)