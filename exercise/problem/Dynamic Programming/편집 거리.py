# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 21.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 최소 편집 거리(Edit Distance) 계산을 위한 다이내믹 프로그래밍
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # dp 테이블 초기화
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # DP 테이블 초기 설정
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
    
    # 최소 편집 거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같다면, 왼쪽 위의 해당하는 수 대입
            if str1[i-1] == str2[i-1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 3가지 경우 증에서 최솟값 찾기
            else: #삽입(왼쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))

  
    
    
  