# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    persons = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first *= 10000 // len(first)
    second *= 10000 // len(second)
    third *= 10000 // len(third)

    f_score, s_score, t_score = 0, 0, 0

    for f, s, t, answer in zip(first, second, third, answers):

        if f == answer: f_score += 1
        if s == answer: s_score += 1
        if t == answer: t_score += 1

    score_list = [f_score, s_score, t_score]
    max_score = max(score_list)

    for i in range(len(score_list)):
        if score_list[i] == max_score:
            persons.append(i + 1)

    return persons


def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == first[idx % len(first)]:
            scores[0] += 1

        if answer == second[idx % len(second)]:
            scores[1] += 1

        if answer == third[idx % len(third)]:
            scores[2] += 1

    for idx, s in enumerate(scores):
        if s == max(scores):
            result.append(idx+1)

    return result



























# def solution(answers):
#     answer = []
#     first = [1, 2, 3, 4, 5] * 2000
#     second = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
#     third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
#
#     cnt1, cnt2, cnt3 = 0, 0, 0
#
#     for i in range(len(answers)):
#         if first[i] == answers[i]: cnt1 += 1
#         if second[i] == answers[i]: cnt2 += 1
#         if third[i] == answers[i]: cnt3 += 1
#
#     max_cnt = max(max(cnt1, cnt2), cnt3)
#     if max_cnt == cnt1: answer.append(1)
#     if max_cnt == cnt2: answer.append(2)
#     if max_cnt == cnt3: answer.append(3)
#
#     print(answer)
#     return answer