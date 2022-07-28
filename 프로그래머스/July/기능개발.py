'''
기능개발 (프로그래머스)
https://school.programmers.co.kr/learn/courses/30/lessons/42586

스택/큐 문제 
'''
from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()
    n = len(progresses)
    for idx, progress in enumerate(progresses):
        q.append((progress, speeds[idx]))

    while q:
        print('전', q)
        cnt = 0
        a, b = q.popleft()

        # 배포할때
        if a >= 100:
            cnt += 1

            for i in range(len(q)):
                c, d = q.popleft()
                if c >= 100:
                    cnt += 1

                else:
                    q.appendleft((c, d))
                    break

            answer.append(cnt)

        # 첫번째 새1끼가 배포할게 아니면 전체 큐에 있는 애들을 업데이트 시켜준다.
        else:
            if not q:
                answer.append(1)
                break

            q.append((a + b, b))
            for i in range(len(q)-1):
                c, d = q.popleft()
                q.append((c + d, d))

        print('후', q)

    print(answer)

    return answer


solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
# solution([93, 30, 55], [1, 30, 5])
