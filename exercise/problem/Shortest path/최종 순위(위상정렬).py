from collections import deque
# star 모양으로 각 노드를 만들어 준 후
# 순위가 높으면 모든 노드에 방향 그래프를 그어주고, 낮은 순위는 indegree를 하나씩 추가해준다
# 그 정보를 가지고 상대적인 순위가 변경되면은 간선의 방향을 뒤집어준다(진입차수도 바뀌겠죠)
# 그 후 위상정렬 수행 (싸이클 발생 -> impossible, 정렬결과가 여러개 -> 큐에 동시에 들어있는 노드가 2개이상일떄 -> ?)

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False]*(n+1) for i in range(n+1)]
    data = list(map(int, input().split()))

    # 방향 그래프의 간선 정보 최소화 ( 순위가 높을 수록 방향이 많아짐)
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())

        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지 여부
    cycle = False # 싸이클 존재 여부

    for i in range(n):
        # 큐가 비어있다면 사이클이 발생
        if len(q) == 0:
            cycle = True
            break

        #  큐의 원소가 2개 이상이면, 정렬 결과가 여러 개
        if len(q) >= 2:
            certain = False
            break

        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for j in range(1, n+1):
            if graph[now][j]: # j와 연결되어 있으면 true -> j의 진입하수 1씩 빼기
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생 (일관성이 없는 경우)
    if cycle:
        print('IMPOSSIBLE')

    # 정렬 결과가 여러개인 경우
    elif not certain:
        print("?")

    else:
        for i in result:
            print(i, end=' ')
        print()