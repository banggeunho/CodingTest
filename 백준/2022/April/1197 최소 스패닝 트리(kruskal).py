# 최소 스패닝트리를 구하는 크루스칼 알고리즘 문제
# 간선의 정보들을 다 받아 간선의 가중치에 대해서 오름찬순으로 정렬 수행
# 그 후 비용이 작은 것 부터 사이클이 발생하지 않는 경우 하나의 그래프로 만들어간다.
def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    global parent
    a = find(a)
    b = find(b)

    if a < b: parent[b] = a
    else: parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
result = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

for edge in sorted(edges):
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)



