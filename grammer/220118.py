# 코딩테스트 대비 파이썬 문법 공부
# Date : 2022. 01. 18.
# 내가 부족한 부분만 적어버리기~

# 파이썬 내장 함수
# sum 함수는 리스트와 같은 iterable 객체가 입력으로 주어졌을 때 사용가능
# iterable 객체란? 반복 가능한 개체 ex) list, dict, tuple

result = sum([1, 2, 3, 4, 5])
print(result)

# min() 함수
result = min(7, 3, 5, 2)
print(result)

# max() 함수
result = max(7, 3, 5, 2)
print(result)

# eval() 함수는 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과
result = eval('(3+5)*7')
print(result)

# sorted() 함수, key 속성으로 정렬 기준을 명시 가능
# reverse로 정렬된 결과를 뒤집을지의 여부 설정 가능
result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)

# lambda x를 설정하여 value값에 의해 정렬을 하도록 만들기
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)

data = [9, 1, 8, 5, 4]
data.sort()
print(data)

# itertools library
# premutaions (순열), combinations (조합)이 가장 유용하게 사용.
# premutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아
# 일렬로 나열하는 모든 경우(순열)을 계산해준다.
# premutaions는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로
# 변환하여 사용한다.

# permutations(data, r) : r개의 데이터를 뽑아 일렬로 나열하는 모든 경우
# combinations : r개의 데이터를 뽑아 순서 상관 없이 나열하는 모든 경우
# product : r개의 데이터를 뽑아 중복포함하여 일렬로 나열하는 모든 경우
#    * repeat 속성을 넣어 뽑고자 하는 데이터수를 넣어줌
#    * product(data, repeat = 2)
# combinations_with_replacement : r개의 데이터를 순서 고려없이 나열하는
# 중복포함합니다.