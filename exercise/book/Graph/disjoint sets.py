# 코딩테스트 대비 기초 문제 풀이 23일차
# Date : 2022. 02. 09.
# Graph Algorithm

# 그래프(Graph)란 노드(Node)와 노드 사이에 연결된 간선(Edge)의 정보를 가지고 있는 자료구조를 의미한다.
# 알고리즘 문제를 접했을 때 '서로 다른 개체(객체)가 연결되어 있다'와 같은 내용이 등장하면 그래프 알고리즘을 의심해보자.

# 그래프와 트리 차이점
# 그래프(네트워크 모델) vs 트리(계층 모델)
# 그래프(부모와 자식 관계 없음) vs 트리(부모와 자식 관계)
# 루트노드가 없음 vs 루트 노드가 존재
# 순환 및 비순환 vs 트리(비순환)

# 서로소 집합(Disjoint sets) : 공통 원소가 없는 두 집합
# 서로소 집합 자료구조란? 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# union(합집합)과 find(찾기) 이 2개의 연산으로 조작할 수 있다.

# 서로소 집합 자료구조는 union-find(합치기- 찾기) 자료구조라고 불리기도 한다.
# 서로소 집합 자료구조를 구현할 때는 트리 자료구조를 이용하여 집합을 표현
# 1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
#  - 1) A와 B의 루트 노드 A', B'를 각각 찾는다.
#  - 2) A'를 B'의 부모 노드로 설정한다.(B'가 A'를 가리키도록 한다.)
# 2. 모든 union 연산을 처리할 때까지 1번 과정을 반복한다.


# 기본적인 서로소 집합 알고리즘 소스

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  # 루트노드의 번호가 더 작은 것으로 바궈줌
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드와 개수와 간선*(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
  print(parent[i], end =' ')



# find_parent 함수가 순서대로 루트 노드를 거슬러 올라가야 하므로 최대 O(V)의 시간이 소요될 수 있다.
# 노드의 개수가 V개이고 FIND 혹은 UNION 연산의 개수가 M일때 O(VM)이 되어 비효율적이다.

# 개선된 서로소 집합 알고리즘 소스코드  
# 특정 원소가 속한 집합을 찾기
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

# 노드와 개수와 간선*(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
  print(parent[i], end =' ')