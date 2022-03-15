# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 15.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 가사 검색
# 2020 카카오 신입 공채 1차

# 단어를 길이 마다 나누어서 저장한다.
# '?'가 문장의 앞에 있을 경우 이진 탐색을 수행 못하기 때문에 뒤집어야 하므로
# reversed_array를 만들어 뒤집어진 words를 길이별로 나눠 저장한다.

# 쿼리마다 하나씩 꺼내서 left를 '?'를 'a'로 right를 'z'로 바꿔서 bisect 로 만든 함수를 집어넣어 단어의 수를 계산한다.
# 반대인 경우는 뒤집어서 수행

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
  answer = []
  for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
    array[len(word)].append(word) # 단어를 삽입
    reversed_array[len(word)].append(word[::-1]) # 뒤집어서 삽입

  for i in range(10001): # 이진 탐색을 위한 각 단어 리스트 정렬 수행
    array[i].sort()
    reversed_array[i].sort()


  for q in queries: # 쿼리를 하나씩 확인하며 처리
    if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
      res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?', 'z'))
    else: # 접두사에 와일드카드가 붙은 경우
      res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?', 'z'))
    answer.append(res)

  return answer




