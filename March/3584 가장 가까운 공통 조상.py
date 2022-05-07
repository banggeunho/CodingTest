# 3584 가장 가까운 공통 조상
# 전형적인 disjoint set 문제
# union, find의 개념을 이해하고 있으면 된다.
# 파이썬의 재귀 제한을 적절하게 해주어야 정답인정이 된다....

import sys
sys.setrecursionlimit(10**4)

def find(parent, x, i):
    global result
    result[i].append(x)
    if parent[x] != x:
        parent[x] = find(parent, parent[x], i)
    return parent[x]


for tc in range(int(input())):
    n = int(input())
    parent = [i for i in range(n+1)]

    for i in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a

    a, b = map(int, input().split())
    result = [[] for i in range(2)]
    find(parent, a, 0)
    find(parent, b, 1)

    solve = False
    for i in result[0]:
        for j in result[1]:
            if i==j:
                print(i)
                solve = True
                break
        if solve:
            break