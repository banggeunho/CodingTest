# 코딩테스트 대비 기초 문제 풀이 29일차
# Date : 2022. 02. 16.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축
def solution(s):   
    answer = len(s)
    split = [i for i in range(1, len(s)//2 + 1)]

    for i in split:
      compressed = ''
      prev = s[0:i]
      count = 1
      for j in range(i, len(s), i):
        if prev == s[j:j+i]:
          count += 1
        else:
          compressed += str(count) + prev if count >=2 else prev
          prev = s[j:j+i]
          count = 1
      # 남아있는 문자열 처리
      compressed += str(count) + prev if count >=2 else prev
      answer = min(answer, len(compressed))
    return answer
  
print(solution('aabbcdefg'))
