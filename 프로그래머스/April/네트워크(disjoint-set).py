parent = []
def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def reload_parent():
    for i in range(len(parent)):
        parent[i] = find_parent(i)

def union_parent(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    global parent
    parent = [i for i in range(n)] # parent initialize 자기자신으로
    for i in range(n):
        for j in range(n):
            if i == j : continue # 자기자신이면 넘어간다.
            if computers[i][j] == 1: # 1인 경우 union
                union_parent(i, j)
    
    # 최종적으로 parent node를 새로고침 해준다.
    reload_parent() 
    answer = len(set(parent))
    return answer