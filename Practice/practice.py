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
