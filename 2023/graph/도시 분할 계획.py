import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i # 부모테이블 자기 자신으로 초기화

edges = [] # 간선 정보 입력 받을 김치통
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() # 크루스칼 알고리즘 쓸 거야!!!
costs = []
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 아닐때
        union_parent(parent, a ,b) # 합칠 거야
        costs.append(cost)

print(sum(costs) - costs[-1]) # 전체 값 중에서 제일 큰 간선 제거
