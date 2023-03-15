N = int(input())

arr = [[0] * N for _ in range(N)]
sequence = []
students = {}
for i in range(N * N):
    data = list(map(int, input().split()))
    sequence.append(data[0])
    students[data[0]] = data[1:]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def count_like_students(x, y, like_students):
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] in like_students:
            count += 1

    return count

def count_empty(x, y):
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            count += 1

    return count


for seq in sequence:

    # 1번 조건
    like_students = students[seq]
    temp_result = []
    max_val = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count = count_like_students(i, j, like_students)

                if max_val < count:
                    max_val = count
                    temp_result.clear()

                if max_val == count:
                    temp_result.append((i, j))

    # 2번 조건
    if len(temp_result) > 1:
        temp2_result = []
        max_val = 0
        for i, j in temp_result:
            count = count_empty(i, j)
            if max_val < count:
                max_val = count
                temp2_result.clear()

            if max_val == count:
                temp2_result.append((i, j))

        # 3번 조건
        if len(temp2_result) > 1:
            temp2_result.sort()

        x, y = temp2_result[0]
    else:
        x, y = temp_result[0]

    # 자리 배치
    arr[x][y] = seq

    # print('1번조건: ', temp_result)
    # print('2번조건: ', temp2_result)
    # print(arr)
    # print('==========')

result = 0
for i in range(N):
    for j in range(N):
        count = count_like_students(i, j, students[arr[i][j]])
        if count == 1:
            result += 1
        elif count == 2:
            result += 10
        elif count == 3:
            result += 100
        elif count == 4:
            result += 1000
# print(arr)
print(result)