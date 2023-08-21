# https://school.programmers.co.kr/learn/courses/30/lessons/118666

from collections import defaultdict


def solution(survey, choices):
    answer = ''
    score = {'R': 0, 'T': 0,
             'C': 0, 'F': 0,
             'J': 0, 'M': 0,
             'A': 0, 'N': 0}

    for s, choice in zip(survey, choices):

        if choice < 4:
            score[s[0]] += (4 - choice)

        elif choice > 4:
            score[s[1]] += (choice - 4)

    print(score)

    if score['T'] <= score['R']:
        answer += 'R'
    else:
        answer += 'T'

    if score['F'] <= score['C']:
        answer += 'C'
    else:
        answer += 'F'

    if score['M'] <= score['J']:
        answer += 'J'
    else:
        answer += 'M'

    if score['N'] <= score['A']:
        answer += 'A'
    else:
        answer += 'N'

    return answer