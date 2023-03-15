N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_result = float('inf')
team = []

# 한 팀의 정보만 구하면 나머지 팀은 따로 확인 할 필요가 없음.
def cal_diff():
    start_sum = 0
    link_sum = 0

    for i in range(N-1):
        for j in range(i+1, N):
            if i in team and j in team:
                start_sum += (arr[i][j] + arr[j][i])
            elif i not in team and j not in team:
                link_sum += (arr[i][j] + arr[j][i])

    return abs(start_sum - link_sum)

def dfs(depth, idx):
    global min_result

    if len(team) == N//2:
        result = cal_diff()
        min_result = min(min_result, result)
        return

    # 팀 구성하기.
    for i in range(idx, N):
        if i not in team:
            team.append(i)
            dfs(depth + 1, i + 1)
            team.pop()

dfs(0, 0)
print(min_result)