# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 12.
# Binary Search
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

from bisect import bisect_left, bisect_right
def countNum(arr, a):
  left = bisect_left(arr, a)
  right = bisect_right(arr, a)

  if right-left == 0:
    return -1
    
  return right - left


n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(countNum(arr, x))

  
    
    