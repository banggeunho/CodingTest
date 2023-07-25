# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 한명의 과학자의 논문 n편 중, h 번 이상 인용된 논문이 h편 이상,
# 나머지 논문은 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 h-index
def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx

    return len(citations)

def solution(citations):
    citations.sort()
    start = 0
    end = citations[-1]

    while start <= end:
        h = (start + end) // 2
        print(h, start, end)
        cnt = 0
        for citation in citations:
            if citation >= h:
                cnt += 1

        print(cnt)
        if cnt >= h:
            start = h + 1

        else:
            end = h - 1

    return end







































import bisect
def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for h in range(1, 10001):
        if h <= n - bisect.bisect_left(citations, h):
            answer = h
    return answer