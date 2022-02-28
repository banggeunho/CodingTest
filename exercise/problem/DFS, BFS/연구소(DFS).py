# 코딩테스트 대비 기초 문제 풀이 40일차
# Date : 2022. 02. 28.
# 구현 문제 풀이
# https://www.acmicpc.net/problem/14502
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 백준 14502번
# 연구소
import itertools
import copy

n, m = map(int, input().split())
arr = []
free = []
virus = []
for i in range(n):
  arr.append(list(map(int, input().split())))
  for j in range(m):
    if arr[i][j] == 0:
      free.append((i, j))
    elif arr[i][j] == 2:
      virus.append((i, j))

def dfs(arr, x, y):
  arr[x][y] = 2
  # 범위를 벗어나지 않을때까지
  if x+1 <= n-1:
    # 아래에 벽이 없다면
    if arr[x+1][y] != 1 and arr[x+1][y] != 2:
      dfs(arr, x+1, y)
  if x-1 >= 0:
    # 위쪽에 벽이 없다면
    if arr[x-1][y] != 1 and arr[x-1][y] != 2:
      dfs(arr, x-1, y)

  if y-1 >= 0:
    # 왼쪽에 벽이 없다면
    if arr[x][y-1] != 1 and arr[x][y-1] != 2:
      dfs(arr, x, y-1)

  if y+1 <= m-1:
    # 우측에 벽이 없다면
    if arr[x][y+1] != 1 and arr[x][y+1] != 2:
      dfs(arr, x, y+1)

  return arr

cases = list(itertools.combinations(free, 3))
answer = 0
# 케이스 별로
for case in cases:
  temp = copy.deepcopy(arr)
  count = 0
  for x,y in case:
    temp[x][y] = 1
    
  for a, b in virus:
    temp = dfs(temp, a, b)

  # print(temp)
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        count += 1
          
  answer = max(answer, count)
  
print(answer)
  


  
  