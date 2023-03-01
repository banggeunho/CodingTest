
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
team = [0] * (n+1) # 팀 초기화

for i in range(1, n+1):
    team[i] = i # 자기 자신으로 초기화

for i in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union_parent(team, a, b)
    else:
        if find_parent(team, a) == find_parent(team, b):
            print("YES")
        else:
            print("NO")


# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1