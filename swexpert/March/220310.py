# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 10.
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------
# 3376 파도반 수열
for tc in range(1, int(input())+1):
  n = int(input())
  arr = [1,1,1,2,2]
  for i in range(len(arr)-1, n):
    arr.append(arr[i]+arr[i-4])
  print(f'#{tc} {arr[n-1]}')


# 3314 보충학습과 평균
for tc in range(1, int(input())+1):
  students = list(map(int, input().split()))
  total = 0
  for score in students:
    if score < 40:
      score = 40
    total += score
  print(f'#{tc} {total//len(students)}')