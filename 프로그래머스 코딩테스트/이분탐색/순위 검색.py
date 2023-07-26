# https://school.programmers.co.kr/learn/courses/30/lessons/72412
import bisect
from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    people = defaultdict(list)

    # 경우의 수를 미리 만들어 놓기
    for i in info:
        person = i.split(" ")
        score = int(person.pop())
        # 풀 텍스트 점수 넣어두기
        people[''.join(person)].append(score)

        # 경우의 수 뽑아서 점수 넣어두기 (괄호포함인 경우)
        for j in range(4):
            case = list(combinations(person, j))
            for c in case:
                people[''.join(c)].append(score)

    # 각 점수 소팅
    for i in people:
        people[i].sort()

    # 쿼리를 하나하나씩 줄여 키로 만들고, 해당 값을 찾아온다 O(1), 그리고 bisect_left를 사용하여 갯수 찾기
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace("and", "").replace(" ", "").replace('-', '')
        answer.append(len(people[key]) - bisect.bisect_left(people[key], score))

    return answer