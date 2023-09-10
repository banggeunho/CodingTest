# https://www.acmicpc.net/problem/15657

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
        if (result and result[-1] <= nums[i]) or not result:
            result.append(nums[i])
            dfs(visited, depth + 1, result)
            result.pop()


dfs(visited, 0, [])
for ans in sorted(answer):
    print(*ans)