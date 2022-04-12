def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v = int(input())
e = int(input())
parent = [i for i in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(a, b)

cnt = 0
for i in range(2, v+1):
    if find_parent(i) == find_parent(1):
        cnt+=1
print(cnt)