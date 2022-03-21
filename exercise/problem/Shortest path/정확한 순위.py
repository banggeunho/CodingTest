# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 21.
# Shortest path
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------


# 정확한 순위
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    graph[k][k] = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
# 자신이 도달 할 수 있거나, 다른 학생이 도달할 수 있으면 순위를 알 수 있다.
# 이 연결이 n만큼 달성되면 정확한 순위를 알 수 있으므로 결과값을 +1 해준다.
for a in range(1, n+1):
    count = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
    if count == n:
        result += 1

print(result)

  

  