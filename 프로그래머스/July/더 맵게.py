'''
더 맵게(프로그래머스)
https://school.programmers.co.kr/learn/courses/30/lessons/42626
힙소트 문제 + 간단한 조건 추가
'''
import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)

    while q:
        a = heapq.heappop(q)
        if a >= K:
            return answer
        
        if q:
            b = heapq.heappop(q)
            heapq.heappush(q, a + (b*2))
        else:
            break
            
        answer += 1

    return -1