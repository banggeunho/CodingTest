# https://school.programmers.co.kr/learn/courses/30/lessons/42861
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


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 비용 순으로 정렬
    parent = [i for i in range(n)]  # 자기 자신을 부모노드로 초기화

    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

        if len(set(parent)) == 1: # 모든 섬이 다 연결되었을 경우 break
            break

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))