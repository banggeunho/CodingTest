import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, job[::-1])

        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now # 시작 지점을 현재 지점으로 바꾸기
            now += current[0] # 현재 지점에 런타임 시간 더하기
            answer += now - current[1] # 종료지점에서 - 요청지점 빼기
            i += 1 # 작업 완료 갯수 추가
        else: # idle time
            now += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))