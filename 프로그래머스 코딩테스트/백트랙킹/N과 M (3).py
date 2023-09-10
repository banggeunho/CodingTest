# https://www.acmicpc.net/problem/15651

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
visited = [False] * (N + 1)
answer = []
def dfs(visited, depth, result):
    global answer

    if depth == M:
        answer.append(result[:])
        return

    for i in range(1, N + 1):
        result.append(i)
        dfs(visited, depth + 1, result)
        result.pop()


dfs(visited, 0, [])
for ans in answer:
    print(*ans)