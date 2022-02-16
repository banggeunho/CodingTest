# 코딩테스트 대비 기초 문제 풀이 29일차
# Date : 2022. 02. 16.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# https://www.acmicpc.net/problem/18406
# 18406 럭키 스트레이트
arr = list(input())
mid = int(len(arr) / 2)
left_sum = 0
right_sum = 0

for i in range(mid):
  left_sum += ord(arr[i]) - ord('0')

for i in range(mid, len(arr)):
  right_sum += ord(arr[i]) - ord('0')

if left_sum == right_sum:
  print('LUCKY')
else:
  print('READY')