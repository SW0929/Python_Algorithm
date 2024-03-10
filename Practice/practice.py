# 자료형
"""
print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3*(3+1))
"""

# 문자형 자료형
"""
print("풍선")
print("나비"*5)
"""

# boolean 자료형 (참/거짓)
"""
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not 5 > 10)
"""

# 변수
# 애완동물을 소개해 주세요!
"""
name = "연탄"
animal = "강아지"
age = 4
hoppy = "산책"
is_adult = age > 3

print("우리집 "+ animal +"의 이름은 "+ name + "입니다.")
print("연탄이는 "+ str(age) +"살이며, "+ hoppy +"을 아주 좋아합니다.")
#문자열로 출력하기 위해 str()
print(name + "는 어른일까요? " + str(is_adult))
"""
# +가 아닌 , 로 변경해서 사용가능!!
# 다만 ,를 사용하면 빈 칸이 하나 들어감

# Quiz 1) 변수를 이용하여 다음 문장을 출력하시오.
"""
변수명 
: station

변수값 
: "사당", "신도림", "인천공항" 순서대로 입력

출력 문장 
: xx 행 열차가 들어오고 있습니다.

Quiz 정답
station = "사당"
print(station, "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")
"""

# 연산자
"""
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 몫 구하기 1
print(10//3) # 1

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False
"""

# 간단한 수식
"""
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 5 # 1
print(number)
"""

# 숫자 처리 함수
"""
print(abs(-5)) # 5 abs()는 절대 값
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3 round()는 반올림
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4
"""

#랜덤 함수(난수)
"""
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1)
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
"""

# Quiz 2)
"""
당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건 1 : 랜덤으로 날짜를 뽑아야 함
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

정답
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", str(date), "일로 선정되었습니다.")
!! 정수형 str()으로 감싸기 !!
"""

# 문자열
'''
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
'''

# 슬라이싱 (필요한 만큼만 잘라서 사용)
"""
jumin = "990101-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지
"""

# 문자열 처리 함수
"""
python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 출력
print(python.upper()) # 모두 대문자로 출력
print(python[0].isupper()) # 첫 문자가 대문자인지 확인
print(len(python)) # 문자열 길이 출력
print(python.replace("Python", "Java")) # 문자열 변경 replace(변경 전, 변경 후)

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 앞선 문자를 찾은 이후 문자열에서 찾음
print(index)
print(python.find("Python")) # 문자열 가장 앞의 인덱스 값 리턴
# find는 찾는 문자가 없으면 -1, index는 에러 발생!!
print(python.count("n")) # 문자열에서 "n" 총 등장 횟수
"""

# 문자열 포맷
"""
# 방법 1
print("나는 %d살입니다." % 20) # %d : 정수
print("나는 %s을 좋아해요." % "파이썬") # %s : 문자열(string)
print("Apple 은 %c로 시작해요." % "A") # %c : 문자(char)
# %s로 정수, 문자 사용해도 무방
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # {} 내부 숫자는 format()의 인덱스 값
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4
age = 20
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
"""