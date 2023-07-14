def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]

    # 패딩 추가
    arr.insert(0, [0] * columns)  # 맨 위에 패딩 행 추가
    arr.append([0] * columns)  # 맨 아래에 패딩 행 추가
    for row in arr:
        row.insert(0, 0)  # 각 행의 가장 왼쪽에 0 추가
        row.append(0)  # 각 행의 가장 오른쪽에 0 추가

    count = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i][j] = count
            count += 1

    # matrix = [[i * columns + (j + 1) for j in range(columns)] for i in range(rows)]

    for query in queries:
        min_set = set()
        x1, y1, x2, y2 = query

        # 오른쪽으로 이동
        start = prev = arr[x1][y1]
        print('start: ', start)
        for i in range(y1 + 1, y2):  # 인덱스 위치를 맞추기 위해
            min_set.add(prev)
            prev, arr[x1][i] = arr[x1][i], prev
            # print(prev, arr[x1][i])

        # 아래로 이동
        for i in range(x1, x2):  # 인덱스 위치를 맞추기 위해
            min_set.add(prev)
            prev, arr[i][y2] = arr[i][y2], prev
            # print(prev, arr[i][y2])

        # 왼쪽으로 이동
        for i in range(y2, y1, -1): # 인덱스 위치를 맞추기 위해
            min_set.add(prev)
            prev, arr[x2][i] = arr[x2][i], prev
            # print(prev, arr[x2][i])

        # 위로 이동
        for i in range(x2, x1-1, -1): # 인덱스 위치를 맞추기 위해
            min_set.add(prev)
            prev, arr[i][y1] = arr[i][y1], prev
            # print(prev, arr[i][y1])

        # 최솟값 추가
        # print(min_set)
        answer.append(min(min_set))

        # print("회전 끝")

    return answer
