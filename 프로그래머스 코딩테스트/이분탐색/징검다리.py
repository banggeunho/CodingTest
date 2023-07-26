# https://school.programmers.co.kr/learn/courses/30/lessons/43236
def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)

    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2  # 거리의 최솟값을 mid로 설정
        current = 0
        remove_rocks = 0

        for rock in rocks:
            diff = rock - current
            if diff < mid:  # 최솟값 보다 작을 경우
                remove_rocks += 1
            else:  # mid 보다 거리가 길거나 거리가 같으면 제거 x
                current = rock  # 현재 위치를 그 바위로 옮김
            if remove_rocks > n:
                break

        if remove_rocks > n:  # 삭제한 바위가 주어진 갯수 보다 많을 경우
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer





















































# answer = 0
#
# rocks.sort()
# rocks.append(distance)
#
# start, end = 0, distance
# while start <= end:
#     mid = (start + end) // 2  # 거리의 최솟값을 mid로 설정
#     current = 0
#     remove_rocks = 0
#     min_distance = int(1e9)
#
#     for rock in rocks:
#         diff = rock - current
#         if diff < mid:  # 최솟값 보다 작을 경우
#             remove_rocks += 1
#         else:  # mid 보다 거리가 길거나 거리가 같으면 제거 x
#             current = rock  # 현재 위치를 그 바위로 옮김
#             min_distance = min(min_distance, diff)
#
#     if remove_rocks > n:  # 삭제한 바위가 주어진 갯수 보다 많을 경우
#         end = mid - 1
#     else:
#         answer = min_distance
#         start = mid + 1