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

#탈출 문자
"""
# \n : 줄바꿈
print("백문이 불여일견\n 백견이 불여일타")
# \" \' : 문장 내 "" or '' 출력
print("저는 \"나도코딩\" 입니다.")
# \\ : 문장 내에서 \
print("C:\\coding\\Python\\Python_Algorithm>")
# \r : 커서를 맨 앞으로 이동해줌
print("Red Apple\rPine") # PineApple
# \b : 백스페이스 (한 글자 삭제)
print("redd\bApple") # redApple
# \t : 탭
print("Red\tApple")
"""

# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
"""
예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 내 'e' 갯수 + "!" 로 구성
                (naver)             (5)         (1)         (!)
예) 생성된 비밀번호 : nav51!

정답 )
url = "http://youtube.com"
my_str = url.replace("http://","") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
password =  my_str[:3] + str(len(my_str)) +str(my_str.count('e')) + '!' # 규칙3

print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
"""

# 리스트 []
"""
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # 리스트 멘 뒤 값 추가
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # 원하는 인덱스에 값 삽입
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list) # 리스트를 하나로 합침
print(num_list)
"""

# 사전 {키:값}
"""
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # Key Error!
print(cabinet.get(5)) # None 출력
print(cabinet.get(5, "사용 가능")) # default 값 출력

print(3 in cabinet) # True/False 출력

cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet2.get("A-3"))
print(cabinet2.get("B-100"))

# 새 손님
cabinet2["A-3"] = "김종국"
cabinet2["C-20"] = "조세호" # 만약 키 값이 있을 경우 값 수정 됨
print(cabinet2)

# 간 손님
del cabinet2["A-3"] # 키 삭제
print(cabinet2)

# key 들만 출력
print(cabinet2.keys())
# value 들만 출력
print(cabinet2.values())

# key, value 쌍으로 출력
print(cabinet2.items())

# 목욕탕 폐점
cabinet2.clear()
print(cabinet2)
"""

# 튜플
# - 내용 변경 및 추가 불가
# - 속도가 리스트 보다 빠름
# - 변경되지 않는 블록 사용시 유리
"""
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "운동"
print(name, age, hobby)

(name, age, hobby) = ("유재석", 50, "토크")
print(name, age, hobby)
"""

# 집합 (set) {}
# 중복 안됨, 순서 없음
"""
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java 도 할 수 있거나 python 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊어버림
java.remove("김태호")
print(java)
"""

# 자료구조의 변경
"""
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
"""

# Quiz 4)
"""
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
 -- 담청자 발표 --
 치킨 당첨자 : 1
 커피 당첨자 : [2, 3, 4]
  -- 축하합니다 --

(활용 예제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1)) # 첫 번째 인자에서 두 번째 인자만큼 뽑겠다.

정답)
from random import *
lst = list(range(1, 21)) # 1부터 20 까지 숫자를 생성
shuffle(lst)
winners = sample(lst, 4)
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")
"""

# if
# if 조건:
#     실행 명령문
"""
weather = input("오늘 날씨는 어때요? ")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
"""

# for
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행 문장
# range(시작, 끝)
# range(끝)
"""
for waiting_num in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_num))

for waiting_num in range(1, 6):
    print("대기번호 : {0}".format(waiting_num))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
"""

# while
# while (조건) 조건에 만족하면 계속 실행
"""
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer= "아이언맨"
index = 1
while True:
     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
"""

# continue 와 break
"""
absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
"""

# 한 줄 for
"""
students = [1, 2, 3, 4, 5]
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [i+100 for i in students]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students] # 리스트 내용을 반복하며 문자열의 길이 출력
print(students)
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students] # 모든 글자 대문자로 변경
print(students)
"""

# Quiz 5) 
"""
당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는
프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분

# 정답 )

from random import *
total_customer = 0 # 총 탑승 승객
for i in range(1, 51):
    customer = randint(5, 50) # 소요시간 5 ~ 50분 랜덤 배정 (조건 1)
    if 5 <= customer <= 15: # 소요시간 5 ~ 15분인 승객 (조건 2)
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, customer))
        total_customer += 1
    else: # 탑승하지 않는 승객
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, customer))

print("총 탑승 승객 : {0} 분".format(total_customer))
"""

# ----- 함수 -----
'''
"""
def 함수명():
   수행내용
"""
def open_account(): # 함수 생성
    print("새로운 계좌가 생성되었습니다.")
open_account() # 함수 호출

# ----- 전달값과 반환값 -----
def deposit(balance, money):
    print("입급이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
    
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# ----- 전달값과 반환값 -----

# ----- 기본값 -----
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" 
          .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")    

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" 
          .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")
# ----- 기본값 -----

# ----- 키워드 값 -----
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")
# ----- 키워드 값 -----

# ----- 가변인자 -----
# 기본 함수
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # 문장 마지막에 end=" " 을 적으면 다음 코드를 이어서 출력하게 한다.
    print(lang1, lang2, lang3, lang4, lang5)

# 가변 인자를 사용한 함수
def profile(name, age, *language): # 서로 다른 갯수의 값을 넣을 때 *매개변수 사용
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # 문장 마지막에 end=" " 을 적으면 다음 코드를 이어서 출력하게 한다.
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "kotlin", "Swift")
# ----- 가변인자 -----

# ----- 지역변수와 전역변수 -----
"""
지역변수 : 함수가 호출될 때 만들어지며 함수가 끝나면 사라짐.
전역변수 : 프로그램 내 모든 공간에서 호출 가능한 변수.
※ 일반적으로 전역변수를 많이 사용하지 않음.(코드 관리가 어려워짐.)
"""
gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    # gun = 20 지역 변수
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun , 2)
print("남은 총 : {0}". format(gun))
# ----- 지역변수와 전역변수 -----
'''
# ----- 함수 -----

# Quiz 6) 표준 체중을 구하는 프로그램을 작성하시오.
"""
* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) X 키(m) X 22
여자 : 키(m) X 키(m) X 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.


# 정답 1)
def std_weight(height, gender):
    if gender == "남자":
        average_weight = height * height * 22 # 남자
    else:
        average_weight = height * height * 21 # 여자

    print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, average_weight))
    # {2:.2f} 는 콜론 앞 숫자는 format index, 뒤 숫자는 소숫점 2까지 출력
    # 즉, 소숫점 3번째 자리를 반올림 하여 출력한다.

std_weight(175/100, "남자")

# 정답 2) 이게 더 맞음
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22 # 남자
    else:
        return height * height * 21 # 여자

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
"""

# 표준 입출력
"""
print("Python", "Java", sep=",") # Python,Java 즉 콤마 부분에 구분자 입력
print("무엇이 더 재밌을까요", end="?") # 뒷 문장을 붙여서 출력
import sys
print("Python", "Java", file=sys.stdout) # 표준 출력으로 문장이 찍힘
print("Python", "Java", file=sys.stderr) # 표준 에러로 출력

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subhect, score in scores.items(): # 키, 값을 쌍을 보내줌
    #print(subhect, score)
    print(subhect.ljust(8), str(score).rjust(4), sep=":")
    # ljust(숫자) : 숫자만큼의 공간을 확보하고 왼쪽 정렬
    # rjust(숫자) : 숫자만큼의 공간을 확보하고 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill(숫자) : 숫자 만큼의 공간을 확보하고 값이 없는 부분은 0을 채움

answer = input("아무 값이나 입력하세요 : ") # 기본 타입은 string
"""

# 다양한 출력포맷
"""
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))
"""

# 파일 입출력
"""
score_file = open("score.txt", "w", encoding="utf8") # w 는 write
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 항상 파일을 열면 닫기 까지

score_file = open("score.txt", "a", encoding="utf8")
# a = append (내용이 존재하는 파일에 이어서 쓰겠다. 동일한 이름 파일에 w 를 쓰면 덮어쓰기 됨.)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")

score_file = open("score.txt", "r", encoding="utf8") # r = read
print(score_file.read()) # 모든 내용 불러오기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄바꿈 안함.
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 파일이 몇 줄인지 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()
"""

# pickle (프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해주는 것.)
"""
import pickle
profile_file = open("profile.pickle", "wb") # b 는 binary
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

# 파일에서 pickle로 데이터를 가지고 오는 작업
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
"""

# with
"""
import pickle
# with 문 탈출 시 자동으로 close()
# 위와 같이 pickle을 사용하는 것 보다 코드 길이도 간단해지고 매번 close()를 안해도 됨.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
"""

# Quiz 7)
"""
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# 정답 )
import pickle

for week in range(1, 51):
    with open("%d주차.txt" % week, "w", encoding="utf8") as report_file:
        report_file.write("- %d 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : " % week)
"""

# ----- 클래스 -----
"""
# 연관있는 변수, 함수들의 집합
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ (생성자 : 객체가 생성될 때 자동으로 만들어 지는 부분)

# ----- 멤버변수 ----- 
#클래스 내에 정의된 변수
# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# 윗줄과 같이 변수명.멤버변수 형태로 외부에서 사용할 수 있다.

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True 
# 클래스 외부에서 원하는 변수를 확장할 수 있으며 확장된 변수는 확장한 객체만 적용.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.")
# ----- 멤버변수 ----- 
"""
# ----- 클래스 -----

# 메소드
"""
# 특정 객체에 종속하는 함수
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
    # attack 과 damaged 는 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25) # hp = 0, 파괴
"""

# 상속
"""
class Unit: # 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
# 공격 유닛
class AttackUnit(Unit): # Unit 상속받음, 자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit 멤버 변수 사용
        self.damage = damage
    
    # attack 과 damaged 는 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25) # hp = 0, 파괴
"""

# 다중 상속
"""
class Unit: # 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
# 공격 유닛
class AttackUnit(Unit): # Unit 상속받음, 자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit 멤버 변수 사용
        self.damage = damage
    
    # attack 과 damaged 는 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))
        
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        # 멤버변수 초기화
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
'''
위의 클래스들 상속 현황
FlyableAttackUnit -> AttackUnit -> Unit
                  -> Flyable
'''
"""

# 메소드 오버라이딩
"""
메소드 오버로딩(확장) : 메소드의 이름은 같지만 매개변수의 개수나 타입이 반드시 달라야한다.
메소드 오버라이딩(재정의) : 메소드의 이름, 매개변수, 반환형이 같은 경우 상속받은 메소드를 자식클래스에서 덮어쓴다.
"""