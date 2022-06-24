n, m, b = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = [int(1e9), 0] # 최소 시간과 높이를 저장할 리스트
for h in range(257): # 모든 높이에 대해서 탐색
    solve = True
    remove = 0
    build = 0
    for i in range(n):
        for j in range(m):
            if h > arr[i][j]: # 정한 높이보다 작을 경우, 설치할 블록의 갯수 저장
                build += (h - arr[i][j])

            else: # 정한 높이보다 클 경우, 지우는 블록의 갯수 저장
                remove += (arr[i][j] - h)

    if (remove + b) >= build: # 블록으로 땅을 고르게 할 수 있는 경우일 때에만
        time = remove * 2 + build # 시간 계산
        if answer[0] >= time: # 정답 업데이트 (최소 시간, 최대 높이)
            answer[0], answer[1] = time, h

print(answer[0], answer[1])