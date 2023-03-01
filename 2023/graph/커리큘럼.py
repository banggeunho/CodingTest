from collections import deque
import copy

n = int(input())
# 진입차수는 모두 0으로 초기화
indegree = [0] * (n+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(n + 1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (n+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 시간 정보 추출
    for j in data[1:-1]:  # 시간 정보, -1 제외
        indegree[i] += 1 # 진입차수 증가
        graph[j].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[now] + time[i], result[i]) # key point
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

