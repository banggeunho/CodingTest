# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    start = 0
    end = n * max(times)

    while start <= end:

        mid = (start + end) // 2

        # 무언가 있어야함
        # 심사가 가능한지 안한지 확인을 해야함.
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            end = mid - 1

        elif people < n:
            start = mid + 1

    return answer



# answer = 0
# start, end = 1, max(times) * n
#
# while start <= end:
#     mid = (start + end) // 2
#     people = 0
#     for time in times:
#         people += mid // time
#
#         if people >= n:
#             break
#
#     if people >= n:
#         answer = mid
#         end = mid - 1
#
#     elif people < n:
#         start = mid + 1