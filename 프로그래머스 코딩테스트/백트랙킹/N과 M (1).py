# https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
visited = [False] * (N + 1)
answer = []
def dfs(visited, depth, result):
    # print(visited, depth, result)
    global answer

    if depth == M:
        answer.append(result[:])
        return answer

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(visited, depth + 1, result)
            result.pop()
            visited[i] = False


dfs(visited, 0, [])
for ans in answer:
    print(*ans)

