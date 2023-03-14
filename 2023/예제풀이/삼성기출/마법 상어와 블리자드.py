# n 지도 크기, m 마법 시전 수
n, m = map(int, input().split())

# 구슬이 없는 경우 0, 상어가 있는 경우도 0
arr = [list(map(int, input().split())) for _ in range(n)]
cmds = [tuple(map(int, input().split())) for _ in range(m)]

# recent = 100
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

m_dx = [0, -1, 1, 0, 0]
m_dy = [0, 0, 0, -1, 1]


def ice_attack(d, s):
    attack_idx = []
    # 공격받은 구슬은 -1로 지정
    sx, sy = n//2, n//2

    for i in range(1, s+1):
        dx, dy = sx + i*m_dx[d], sy + i*m_dy[d]
        arr[dx][dy] = -1

def list_marble():
    result = []
    # 변수 초기화
    stack = 2  # n칸씩 이동하는 횟수, 스택이 0이되면 count 증가
    count = 1
    direction = 0
    time = 0
    x, y = n // 2, n // 2
    while True:

        x, y = x + dx[direction], y + dy[direction]
        if  x < 0 or x >= n or y < 0 or y >= n:
            break
        result.append(arr[x][y])
        time += 1

        # 해당 시간이 지나면 방향 전환
        if time == count:
            direction = (direction + 1) % 4
            stack -= 1
            time = 0
            if stack == 0:
                count += 1
                stack = 2
    return result

def resotre_marble(temp):
    # 변수 초기화
    stack = 2  # n칸씩 이동하는 횟수, 스택이 0이되면 count 증가
    count = 1
    direction = 0
    time = 0
    i = 0
    x, y = n // 2, n // 2
    while True:

        x, y = x + dx[direction], y + dy[direction]
        if  x < 0 or x >= n or y < 0 or y >= n:
            break

        if len(temp) <= i:
            arr[x][y] = 0
        else:
            arr[x][y] = temp[i]

        i += 1
        # result.append((x, y, arr[x][y]))
        time += 1

        # 해당 시간이 지나면 방향 전환
        if time == count:
            direction = (direction + 1) % 4
            stack -= 1
            time = 0
            if stack == 0:
                count += 1
                stack = 2


count_one = 0
count_two = 0
count_three = 0

for d, s in cmds:
    ice_attack(d, s)
    temp = list_marble()

    # 구슬 복구
    del_cnt = temp.count(-1)
    moved_marble = [marble for marble in temp if marble != -1]
    moved_marble.extend([0] * del_cnt)


    # 구슬 복구하기 4개 이상 연속된게 없을때 까지 터치기~
    coll_idx = [(1,1)]
    while len(coll_idx) > 0:
        # 구슬 폭파시키기
        coll_idx = []
        count = 1
        start = 0
        for i in range(len(moved_marble)-1):
            # 다른게 발견 됐을 시
            if moved_marble[i] != moved_marble[i+1]:
                # 4개 이상일 시 폭파
                if count >= 4:
                    if moved_marble[i] == 1:
                        count_one += count
                    elif moved_marble[i] == 2:
                        count_two += count
                    elif moved_marble[i] == 3:
                        count_three += count
                    coll_idx.append((start, i))
                start = i + 1
                count = 1

            else:
                count += 1


        # 구슬 붙이기
        result_marble = []
        previous = 0
        for i, j in coll_idx:
            result_marble += moved_marble[previous:i]
            previous = j+1
        result_marble += moved_marble[previous:]
        moved_marble = result_marble

    # 구슬 그룹핑, 정리
    new_marble = []
    count = 1
    for i in range(len(moved_marble) - 1):
        # 다른게 발견 됐을 시
        if moved_marble[i] != moved_marble[i + 1]:
            new_marble.append(count)
            new_marble.append(moved_marble[i])
            count = 1

        else:
            count += 1

    resotre_marble(new_marble)
    # print(arr)

print(count_one + 2*count_two + 3*count_three)
