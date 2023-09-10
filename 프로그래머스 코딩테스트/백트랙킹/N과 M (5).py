# https://www.acmicpc.net/problem/15654

N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False] * (N + 1)
answer = []
def dfs(visited, depth, result):
    global answer

    if depth == M:
        answer.append(result[:])
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])
            dfs(visited, depth + 1, result)
            result.pop()
            visited[i] = False


dfs(visited, 0, [])
for ans in sorted(answer):
    print(*ans)