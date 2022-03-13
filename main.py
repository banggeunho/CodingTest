# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 14.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 두 수의 덧셈 3260
for tc in range(1, int(input())+1):
  a, b = map(int, input().split())
  print(f'#{tc} {a+b}')
    