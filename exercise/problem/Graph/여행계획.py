#  여행 계획 ( 같은 집합에 속하지 않으면 된 것)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(i, n):
        if arr[j] == 1:
            union_parent(parent, i+1, j+1)


plan = list(map(int, input().split()))
solve = True
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        solve = False
        print('NO')
        break

if solve:
    print('YES')