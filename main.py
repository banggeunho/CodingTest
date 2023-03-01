# 코딩테스트 대비 기초 문제 풀이
# Date : 2022. 11. 6.

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****--------------------------------------------

from collections import deque

# 
def catch(arr):
  arr.popleft()
  return arr

# 오른쪽으로 이동
def mv_right(arr, idx):
  cnt = 0
  while dq[0] != idx:
    arr.appendleft(arr.pop())
    cnt += 1
  return arr, cnt

# 왼쪽으로 이동
def mv_left(arr, idx):
  cnt = 0
  while dq[0] != idx:
    arr.append(arr.popleft())
    cnt += 1 
  return arr, cnt

n, m = map(int, input().split())
idxs = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])
result = 0

while idxs:
  # print("=====================")
  # print(dq)
  idx = idxs.pop(0)
  # arr = catch(arr)

  if(dq.index(idx) == 0):
    dq = catch(dq)
    
  else:
    idxs.insert(0, idx)
    if(dq.index(idx) < len(dq)/2): # 왼쪽으로 이동하는게 더 가까울 경우
      dq, cnt = mv_left(dq, idx)
      result += cnt
      # print(cnt)
    else:
      dq, cnt = mv_right(dq, idx)
      result += cnt
      # print(cnt)

print(result)
  


