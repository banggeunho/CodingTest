# https://school.programmers.co.kr/learn/courses/30/lessons/68644
from itertools import combinations
def solution(numbers):
    answer = set()
    cases = list(combinations(numbers, 2))
    for case in cases:
        answer.add(sum(case))

    return sorted(list(answer))

def solution(numbers):
    return sorted(set(map(sum, combinations(numbers, 2))))