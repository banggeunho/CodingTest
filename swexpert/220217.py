# 코딩테스트 대비 기초 문제 풀이 32일차
# Date : 2022. 02. 17.
# 구현 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------

# 9088. 다이아몬드

for i in range(1, int(input())+1):
  n, k = map(int, input().split())
  diamond = list()
  temp = list()
  max_diamond = 0
  for j in range(n):
    diamond.append(int(input()))

  diamond.sort()
  
  for j in range(0, len(diamond)):
    temp = []
    temp.append(diamond[j])
    for l in range(j+1, len(diamond)):
      if diamond[l] - diamond[j] <= k:
        temp.append(diamond[l])
      
      else:
        break

    max_diamond = max(max_diamond, len(temp))
    

  print(f'#{i} {max_diamond}')
    
      

    
# 7465. 창용 마을 무리의 개수
# 서로소 집합 문제
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  # 루트노드의 번호가 더 작은 것으로 바궈줌
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for tc in range(1, int(input())+1):
  # 노드와 개수와 간선*(union 연산)의 개수 입력 받기
  n, m = map(int, input().split())
  parent = [0] * (n + 1) # 부모 테이블 초기화

  # 부모 테이블상에서, 부모를 자기 자신으로 초기화
  for i in range(1, n+1):
    parent[i] = i

  # union 연산을 각각 수행
  for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

  # 각 원소가 속한 집합 출력
  team = []
  for i in range(1, n+1):
    team.append(find_parent(parent, i))

  result = set(team)
  result = list(result)
  print(f'#{tc} {len(result)}')

# 12052 부서진 타일
for tc in range(1, int(input())+1):
  n, m = map(int, input().split())
  arr = []
  solve = True

  for i in range(n):
    arr.append(list(input()))


  for i in range(n-1):
    for j in range(m-1):
      # print(arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1])
      if arr[i][j] == '#' and arr[i][j+1] == '#' and arr[i+1][j] == '#' and arr[i+1][j+1] == '#':
        arr[i][j] = '.'
        arr[i][j+1] = '.'
        arr[i+1][j] = '.'
        arr[i+1][j+1] = '.'

  for i in range(n):
    for j in range(m):
      if arr[i][j] == '#':
        solve = False
        break
  if not solve:
    print(f'#{tc} NO')
  else:
    print(f'#{tc} YES')


