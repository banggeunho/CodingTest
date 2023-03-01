## kruskal algorithm O(ElogE) : E(edge)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

# 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i # 자기 자신을 부모노드로 초기화


# 간서에 대한 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용 순으로 정렬 하기 위함

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,  b)
        result += cost
    else:
        print(' 싸이클 발생 ', a, b)

print(result)


# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25