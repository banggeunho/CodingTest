def solution(p):
    answer = [0] * len(p)

    for i in range(len(p)):
        temp = int(1e9)
        temp_idx = -1
        for j in range(i, len(p)):
            if p[j] < temp:
                temp = p[j]
                temp_idx = j

        if i != temp_idx:
            answer[i] += 1
            answer[temp_idx] += 1
            p[i], p[temp_idx] = p[temp_idx], p[i]

    print(answer)
    return answer


solution([2, 5, 3, 1, 4])


# periods 가입기간
# payments 납부내역
# estimates 납부 예정

# 이번달에는 vip가 아니지만 다음달에 vip되는 수
# 이번달에는 vip이지만 다음 달에는 vip가 아닌 고객

# vip가 되는 조건 2년 이상(24개월) ~ 5년미만 (90만원 이상)
# vip가 되는 조건 5년 이상(60개월) ~ 5년이상 (60만원 이상)

# binary search?..

def solution(periods, payments, estimates):
    users = [[] for _ in range(len(periods))]
    for i in range(len(periods)):  # 유저별로 가입기간 저장
        users[i].append(periods[i])

    for i in range(len(payments)):  # 유저별 최근12개월 납부내역 저장
        users[i].append(sum(payments[i]))

    for i in range(len(users)):  # 현재 vip인지 아닌지 체크
        if (users[i][0] >= 24 and users[i][1] >= 900000) or (users[i][0] >= 60 and users[i][1] >= 600000):
            users[i].append(1)
        else:
            users[i].append(0)

    for i in range(len(users)):  # 다음달 vip인지 아닌지 체크
        temp_periods = periods[i] + 1  # 다음달이기 때문에 1 더하기
        temp_payments = users[i][1] - payments[i][0] + estimates[i]  # 가장 마지막 납부내역 제거 후 다음달 납부내역 더하가
        if (temp_periods >= 24 and temp_payments >= 900000) or (temp_periods >= 60 and temp_payments >= 600000):
            users[i].append(1)
        else:
            users[i].append(0)

    answers = [0, 0]  # [다음달에 vip가 되는 고객, 다음달에 vip에서 짤리는 고객]
    for i in users:
        if i[2] == 0 and i[3] == 1:  # 이번달에는 vip가 아님, 다음달엔 vip
            answers[0] += 1

        elif i[2] == 1 and i[3] == 0:  # 이번달에는 vip이지만, 다음달엔 vip가 아님
            answers[1] += 1

    return answers


# <Requirements>
# 1번~m번 휴대폰 요금제 (m-1개)
# 1번~n번 부가서비스 (n-1개)
# 번호가 높아질 수록 제공하는 데이터가 많아지고, 부가서비스도 많아짐
# 고객별로 고객이 원하는 데이터와 부가서비스를 알고 있을떄, 니즈를 충족하는 가장 작은 요금제의 번호 목록
# 위 조건을 만족하는 요금제가 없는 경우 목록에 0을 담습니다.

# plans의 범위가 30만개 이므로.. binary search 수행

import copy
def solution(n, plans, clients):
    answer = []
    current_plans = [[] for _ in range(len(plans))]
    total_service = []

    # 요금제 만들기
    for i in range(len(plans)):
        data = plans[i].split()
        current_plans[i].append(int(data[0]))

        if len(data) > 0: # 부가서비스 처리 부분
            service = list(map(int, data[1:]))
            total_service = copy.deepcopy(total_service)
            for j in service:
                total_service.append(j)
            current_plans[i].append(total_service)

    # 클라이언트 니즈 확인
    for i in clients:
        data = i.split()
        need_data = int(data[0])
        need_service = list(map(int, data[1:]))

        # binary search 이용하여 조건에 맞는 요금제 탐색 수행
        start = 0
        end = len(current_plans)-1
        while start <= end:
            mid = (start+end)//2
            if need_data <= current_plans[mid][0] and max(need_service) in current_plans[mid][1]:
                end = mid - 1
            else:
                start = mid + 1

        if start < len(current_plans): # 찾았을 경우
            answer.append(start+1)

        else: # 조건을 충족하는 요금제가 아닌 경우
            answer.append(0)
    print(current_plans)
    return answer


solution(5, ['100 1 3', '500 4','2000 5'], ['300 3 5', '1500 1', '100 1 3', '50 1 2'])


arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = 0, 0
answer = int(1e9)
def dfs(x, y, k, visited, sleep):
    print(x, y, k)
    global n, m, answer
    if x == n and y == m:
        answer = min(sleep, answer)
        return

    if k < 0 and not arr[x][y] != '.':
        return

    # elif k == 0 and arr[x][y] == '.':
    #     k = 3
    #     sleep += 1
    #     print('숙영')

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n and 0 <= ny <= m and not visited[nx][ny] and k > 0:
            if arr[nx][ny] != '#':
                visited[nx][ny] = True
                dfs(nx, ny, k-1, visited, sleep)
                visited[nx][ny] = False

def solution(grid, k):
    global n, m
    n = len(grid) - 1
    m = len(grid[0]) - 1
    for i in range(n + 1):
        arr.append(list(grid[i]))

    print(arr)
    visited = [[False] * (m+1) for _ in range (n+1)]
    visited[0][0] = True
    dfs(0, 0, k-1, visited, 0)

    print(answer)
    return answer

solution(['..FF', '###F', '###.'], 4)