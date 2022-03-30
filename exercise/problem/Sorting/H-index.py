#https://programmers.co.kr/learn/courses/30/lessons/42747
# H-index
import bisect
def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for h in range(1, 10001):
        if h <= n - bisect.bisect_left(citations, h):
            answer = h
    return answer