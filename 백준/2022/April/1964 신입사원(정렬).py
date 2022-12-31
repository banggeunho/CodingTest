# 1964번 신입 사원
# 조건에 따라 먼저 서류 순위로 정렬을 한 뒤
# 남은 면접 순위로 비교를 시작
# 면접 순위가 더 낮으면 불합격
for tc in range(int(input())):
    n = int(input())
    arr = []
    cnt = 1
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort()
    criteria = arr[0][1]
    for i in range(1, n):
        if criteria > arr[i][1]:
            criteria = arr[i][1]
            cnt += 1

    print(cnt)