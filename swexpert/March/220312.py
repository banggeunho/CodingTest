# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 12.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 최증증가수열 (Longest Increasing Subsequence)
# Dynamic Programming
# case 1 : 순차탐색으로 하나씩 값을 비교해서 보는 법 O(N^2)
# case 2 : 이진탐색으로 자리의 값을 찾아서 비교해서 보는 법 O(NlogN)

for tc in range(1, int(input())+1):
  n = int(input())
  arr = list(map(int, input().split()))
  dp = [0 for i in range(n)]
  
  long_dis = 0
  for i in range(len(arr)):
    dp[i] = 1
    for j in range(0, i):
      if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
        dp[i] = dp[j] + 1
        long_dis = max(long_dis, dp[i])

  print(f'#{tc} {long_dis}')
    