# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 04.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14888
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 식의 계산은 우선순위 무시하고, 앞에서 부터 연산
# 나눗셈은 정수 나눗셈으로 몫만 취한다(//)
# 음수를 양수로 나눌 시 -> 음수를 양수로 바꿔주고 몫만 취한 뒤 음수로 바꿔 준다.

# 첫째줄에는 수의 개수 N
# 둘째줄에는 N개만큼 수열이 주어지고
# 셋째줄에는 +,-,X,/ 순서대로 갯수가 주어짐 (총 N-1)

# 출력
# 첫째줄 최댓값
# 들쪠즐 최솟값

N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
  global max_value, min_value, add, sub, mul, div

  if i == N:
    max_value = max(max_value, now)
    min_value = min(min_value, now)

  else:
    if add > 0:
      add -= 1
      dfs(i+1, now + arr[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i+1, now - arr[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i+1, now * arr[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i+1, int(now / arr[i]))
      div += 1

dfs(1, arr[0])
print(max_value)
print(min_value)

