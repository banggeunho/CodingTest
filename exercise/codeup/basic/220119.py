# 코딩테스트 대비 코드업 기초 문제 풀이
# Date : 2022. 01. 19.
# 내가 부족한 문법 & 스킬에 대한 기초 문제 풀이

# ASCII 코드
# ord 함수는 문자를 10진수로 바꿔주고
# chr 함수는 10진수를 문자로 바꿔준다.
# a = input()
# a = ord(a)
# print(chr(a+1))

# 공백으로 구분하여 정수 입력받기
# a, b = map(int, input().split())
# print(a-b)

# 실수 2개 입력받아 곱 출력
# a, b = map(float, input().split())
# print(a*b)

# 거듭제곱 출력
# print(a**b)

# 몫 출력
# print(a//b)

# 세번째 자리에서 반올림
# a, b = map(float, input().split())
# print(round(a/b, 3))

# 세번째 자리까지만 출력
# a, b = map(float, input().split())
# print('%.3f' % (a/b))

# 두 정수를 입력받아 줄마다 합,차,곱,몫을 출력

# a, b = map(int, input().split())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print('%.2f' % (a/b))

# 정수 3개를 입력 받아 합과 평균을 공백을 두고 출력
# num = list(map(int, input().split()))
# sum = sum(num)
# avr = round(sum/len(num), 3)
# print('%d %.2f' % (sum, avr))

# n = 10 에서 10 은 10진수 정수 값으로 인식된다.
# 변수 n 에 문자열을 저장하고 싶다면, n = "10" 또는 n = '10'으로 작성해 넣으면 되고,

# n = 10.0 으로 작성해 넣으면 자동으로 실수 값으로 저장된다.
# n = 0o10 으로 작성해 넣으면 8진수(octal) 10으로 인식되어 10진수 8값이 저장되고,
# n = 0xf 나 n = 0XF 으로 작성해 넣으면 16진수(hexadecimal) F로 인식되어 10진수 15값으로 저장된다.

# 예시
# n = 10
# print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
# print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
# print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
# print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# 조건문
# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.
a, b = map(int, input().split())

if b >= a:
  print("True")
else:
  print("False")

