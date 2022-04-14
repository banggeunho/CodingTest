
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
for _ in range(e):
    a, b = map(int, input().split())
    union(a, b)

# 최신화 시켜주는게 뽀인트!
result = [find(i) for i in range(1, v+1)]
print(len(set(result)))


