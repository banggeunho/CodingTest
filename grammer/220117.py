# 코딩테스트 대비 파이썬 문법 공부
# Date : 2022. 01. 17.
# 내가 부족한 부분만 적어버리기~

# 정수형
a,b = 1000, -7
print(a, b)

# 실수형
a, b = 157.93, -154.32
print(a, b)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 10억의 지수 표현 방식
a  = 1e9
print(a)

# 3.954
a = 3954e-3
print(a)

# key point @@@@@@@
# 컴퓨터가 연산을 할 때 2진수를 이용,
# 2진수는 실수형을 정확하게 표기하는데에 한계가 있음.
a = 0.3 + 0.6
print(a)

# 해결방법 -> 반올림 함수이용 / 소수점 4번째에서 반올림
print(round(a, 4))

a, b = 7, 3
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

# list

# 빈 list 선언 (두가지 방법이 존재)
a, b = [], list()
print(a, b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0]*n
print(a)

# list comprehension
# for문과 if문의 아름다운 조화
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = []
for i in range(20):
  if i % 2 == 1:
    array.append(i)
print(array)

array = [i*i for i in range(1, 10)]
print(array)

# 2-dimensional array (n x m) 2차원
n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array)

array[1][1] = 5
print(array)

# 잘못된 2차원 배열 선언 방법
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

# list, 배열 관련 기타 메서드
# append(), sorting(), reverse(), insert(), count(), remove()
# O(1),  O(NlogN), O(N),  O(N),  O(N), O(N)  - Time Complexity

a = [1, 4, 3]
a.append(2)
print('append', a)

a.sort()
print('sorting', a)

a.sort(reverse = True)
print('descending sorting', a)

a.reverse()
print('reverse', a)

a.insert(2, 3)
print('add 3 to index 2', a)

print("count the number of 3", a.count(3))

a.remove(1)
print('remove the data equals to 1', a)

# insert, remove 함수를 남발하면 시간초과가 나올 수 있음.
# 특정한 값의 원소를 모두 제거하려면
# 다른 framework에서는 remove_all을 사용
# 하지만 python에서는 제공하지 않는 함수 이무르
# remove_set을 따로 지정해서 list comprehension을 이용한다

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]
print(result)

# 문자열, SyntaxWarning
string = "hello world"
print(string)

# 따옴표를 쓰려면 백 slash를 넣어줘야한다.
string = 'Dont\'t you know \'Python\'?'
print(string)

# 문자열 연산
a = 'hello'
b = 'world'
print(a+''+b)
print(a*3)
print(a[2:4])

# 튜플 자료형, tuple
a = (1, 2, 3, 4)
print(a)

# 튜플은 한 번 선언된 값을 변경할 수 없음.
# a[2] = 7

# 사전 자료형, dictionary (key-value pairs)
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("'사과'를 key로 가지는 데이터가 존재합니다.")

# 사전 자료형 관련 함수
# 키 데이터만 담은 list
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
  print(data[key])

# 집합 자료형 (중복을 허용하지 않는다, 순서가 없다)
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) #합
print(a & b) #교
print(a - b) #차

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# 반복문
scores = [90, 85, 77, 65, 97]
cheating_list = [2, 4]

for i in range(5):
  if i+1 in cheating_list:
    continue
  if scores[i] >= 80:
    print(i+1, "번 학생은 합격입니다.")


# function, 함수
# a = 0

# def func():
#   global a # global은 내장함수 만들지 않고 밖의 변수를 참조하겠다.
#   a += 1
# for i in range(10):
#   func()
# print(a)

# 람다 표현식으로 구현한 add() method
print((lambda a, b: a+b)(3, 7))

# 입출력
# n = int(input())

# 각 데이터를 공백으로 구분하여 입력
# data = list(map(int, input().split()))

# data.sorting(reverse = True)
# print(data)

# n, m, k = map(int, input().split())
# print(n, m, k)

# python의 input()함수는 동작 속도가 느려서
# 시간초과 발생 가능
# 이 경우 sys 라이브러리의 sys.stdin.readline() 이용
# rstrip()은 마지막 '\n' 값 제거 하는 것임
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# Python 3.6 이상 버전부터 f-string 문법을 사용가능
# 문자열 앞에 f를 붙이면 중괄호 안에 변수를 넣으면
# 자료형의 변환 없이도 간단히 문자열과 정수를 함께 사용
answer = 7
print(f'정답은 {answer}입니다.')