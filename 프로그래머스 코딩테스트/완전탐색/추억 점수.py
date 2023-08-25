# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    scores = {}

    for n, y in zip(name, yearning):
        scores[n] = y

    for p in photo:
        temp_sum = 0
        for name in p:
            if name in scores:
                temp_sum += scores[name]

        answer.append(temp_sum)

    return answer