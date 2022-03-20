# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 20.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 백준 14501 퇴사
n = int(input())
t = []
p = []
dp = [0]*(n+1)
max_value = 0
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n-1, -1, -1):
    # 현재날짜 + 걸리는 날짜
    time = t[i] + i
    if time <= n:
        # 현재 임금 + 시간이 지난후 받을 수 있는 최대 임금
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)


  
    
    
  