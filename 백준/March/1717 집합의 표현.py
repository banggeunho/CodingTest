# 1717 집합의 표현
# 전형적인 disjoint set 문제
# union, find의 개념을 이해하고 있으면 된다.
# 파이썬의 재귀 제한을 적절하게 해주어야 정답인정이 된다....
# 재귀함수 limit을 써도 메모리 초과가 나서, find함수 parameter에서 parent 제거후
# global 변수로 대신 선언해주었다.
import sys
sys.setrecursionlimit(10**5)

def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        union(parent, a, b)
    else:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')



