# 전형적인 구현 문제

op = {'left': 0, 'right': 1, 'up': 2, 'down': 3}

for tc in range(1, int(input())+1):
    data = list(input().split())
    arr = []
    check = []
    n = int(data[0])
    idx = op[data[1]]
    for i in range(n):
        arr.append(list(map(int, input().split())))
    cnt = 0
    while True:
        cnt += 1
        if idx == 0: # left
            for j in range(1, n):
                for i in range(n):
                    if arr[i][j] != 0:
                        if arr[i][j] == arr[i][j-1] and (i, j) not in check and (i,j-1) not in check: # 타일의 수가 같거나 합쳐진 타일이 아니면
                            arr[i][j-1] *= 2 # 밀려질 타일의 값을 곱해준다
                            arr[i][j] = 0 # 밀려진 타일 값은 0으로 초기화
                            check.append((i, j-1)) # 합쳐진 타일 위치 저장

                        # 비어있을 경우
                        elif arr[i][j-1] == 0: # 비어있을 경우
                            arr[i][j-1] = arr[i][j]
                            arr[i][j] = 0
                            if (i, j) in check:
                                check.remove((i, j))
                                check.append((i, j-1))

        elif idx == 1: # right
            for j in range(n - 2, -1, -1):
                for i in range(n):
                    if arr[i][j] != 0:
                        if arr[i][j] == arr[i][j + 1] and (i, j) not in check and (i, j + 1) not in check:  # 타일의 수가 같거나 합쳐진 타일이 아니면
                            arr[i][j + 1] *= 2  # 밀려질 타일의 값을 곱해준다
                            arr[i][j] = 0  # 밀려진 타일 값은 0으로 초기화
                            check.append((i, j + 1))  # 합쳐진 타일 위치 저장

                        # 비어있을 경우
                        elif arr[i][j] !=0 and arr[i][j + 1] == 0:  # 비어있을 경우
                            arr[i][j + 1] = arr[i][j]
                            arr[i][j] = 0
                            if (i, j) in check:
                                check.remove((i, j))
                                check.append((i, j+1))

        elif idx == 2: # up
            for i in range(1, n):
                for j in range(n):
                    if arr[i][j] != 0:
                        if arr[i][j] == arr[i - 1][j] and (i, j) not in check and (i - 1, j) not in check:  # 타일의 수가 같거나 합쳐진 타일이 아니면
                            arr[i - 1][j] *= 2  # 밀려질 타일의 값을 곱해준다
                            arr[i][j] = 0  # 밀려진 타일 값은 0으로 초기화
                            check.append((i - 1, j))  # 합쳐진 타일 위치 저장

                        # 비어있을 경우
                        elif arr[i][j] !=0 and arr[i - 1][j] == 0:  # 비어있을 경우
                            arr[i - 1][j] = arr[i][j]
                            arr[i][j] = 0
                            if (i, j) in check:
                                check.remove((i, j))
                                check.append((i - 1, j))
        elif idx == 3: # down
            for i in range(n - 2, -1, -1):
                for j in range(n):
                    if arr[i][j] != 0:
                        if arr[i][j] == arr[i + 1][j] and (i, j) not in check and (i + 1, j) not in check:  # 타일의 수가 같거나 합쳐진 타일이 아니면
                            arr[i + 1][j] *= 2  # 밀려질 타일의 값을 곱해준다
                            arr[i][j] = 0  # 밀려진 타일 값은 0으로 초기화
                            check.append((i + 1, j))  # 합쳐진 타일 위치 저장

                        # 비어있을 경우
                        elif arr[i][j] !=0 and arr[i + 1][j] == 0:  # 비어있을 경우
                            arr[i + 1][j] = arr[i][j]
                            arr[i][j] = 0
                            if (i, j) in check:
                                check.remove((i, j))
                                check.append((i+1, j))

        if cnt == n+1:
            break
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()