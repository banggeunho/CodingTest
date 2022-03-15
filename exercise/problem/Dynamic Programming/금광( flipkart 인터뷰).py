# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 15.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 금광 (flipkart 인터뷰)
n, m = map(int, input().split())
input = list(map(int, input().split()))
arr = []
dp = [[0]*m for _ in range(n)]

for i in range(0, len(input), m):
  arr.append(input[i:i+m])

for i in range(n):
  dp[i][m-1] = arr[i][m-1]

for i in range(m-2, -1, -1):
  for j in range(n):
    if j !=0 and j != n-1:
      dp[j][i] = max(dp[j][i], arr[j][i]+dp[j][i+1], arr[j][i]+dp[j-1][i+1], arr[j][i]+dp[j+1][i+1])
    elif j==0:
      dp[j][i] = max(dp[j][i], arr[j][i]+dp[j][i+1], arr[j][i]+dp[j+1][i+1])
    else:
      dp[j][i] = max(dp[j][i], arr[j][i]+dp[j][i+1], arr[j][i]+dp[j-1][i+1])

print(dp)
answer = 0
for i in range(n):
  answer = max(answer, dp[i][0])

print(answer)

      