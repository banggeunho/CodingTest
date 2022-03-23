# 최소 신장 트리 문제
# 비용 기준으로 오름차순 정렬 후
# 사이클이 발생하지 않도록 노드 간 연결해준다.

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
parent = [i for i in range(n)]
cost = []
total_cost = 0
for i in range(m):
    a, b, c = map(int, input().split())
    total_cost += c
    cost.append((c, a, b))

cost.sort()

result = 0
for c, a, b in cost:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result +=c

print(total_cost - result)