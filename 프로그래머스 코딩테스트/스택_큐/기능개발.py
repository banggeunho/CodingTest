# https://school.programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()

    for progress, speed in zip(progresses, speeds):
        q.append((progress, speed))

    while q:
        # print(q)
        count = 0
        progress, speed = q.popleft()

        # 배포가 안될 경우
        if progress + speed < 100:
            q.append((progress + speed, speed))
            for i in range(len(q) - 1):
                p, s = q.popleft()
                q.append((p + s, s))

        else:
            count += 1
            for i in range(len(q)):
                p, s = q.popleft()
                if p + s >= 100:
                    count += 1
                else:
                    q.appendleft((p, s))
                    break

            answer.append(count)

    return answer


def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    return answer

























































