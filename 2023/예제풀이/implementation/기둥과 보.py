

def check(answer):
    for x, y, stuff in answer:
        # 기둥인 경우
        if stuff == 0:
            # 바닥에 설치 됐거나, 보의 한 쪽 끝부분 위 혹은 다른 기둥 위라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보인 경우
        else:
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True



n = 3
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
answer = []
# x: 좌표, y: 좌표, a: 구조물(0:기둥, 1:보), b: 작업(0: 삭제, 1: 설치)
for x, y, a, b in build_frame:

    # 삭제 작업
    if b == 0:
        answer.remove([x, y, a])
        if not check(answer):
            answer.append([x, y, a])

    # 설치 작업
    else:
        answer.append([x, y, a])
        if not check(answer):
            answer.remove([x, y, a])


print(sorted(answer))