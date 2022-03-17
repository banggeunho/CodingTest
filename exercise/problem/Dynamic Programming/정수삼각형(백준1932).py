# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 17.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 백준 1932번
# 정수 삼각형
# 다이내믹 프로그래밍으로 접근
n = int(input())
arr = [[]]
dp = [[0]*n for i in range(n)]

arr[0] = int(input())
for i in range(1, n):
  arr.append(list(map(int, input().split())))

dp[0][0] = arr[0]

for i in range(1, n):
  for j in range(i+1):
    if j > 0 and j < i:
      dp[i][j] = max(dp[i][j], arr[i][j]+dp[i-1][j-1], arr[i][j]+dp[i-1][j])

    elif j == 0:
      dp[i][j] = max(dp[i][j], arr[i][j]+dp[i-1][j])

    elif j == i:
      dp[i][j] = max(dp[i][j], arr[i][j]+dp[i-1][j-1])


print(max(dp[n-1]))
    
  