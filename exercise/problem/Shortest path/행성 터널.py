# 주어진 식을 가지고 경우의 수를 줄이는 것이 포인트
# 각 좌표별로 sorting해서 3*(n-1)개의 edge를 골라내어
# 크루스칼 알고리즘을 해주면 된다.
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


n =int(input())
parent = [i for i in range(n)]
edges=[]
x=[]
y=[]
z=[]
for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((abs(x[i][0] - x[i + 1][0]), x[i][1], x[i+1][1]))
    edges.append((abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    edges.append((abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

edges.sort()
result = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result +=c

print(result)