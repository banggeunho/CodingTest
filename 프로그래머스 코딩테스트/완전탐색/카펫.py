# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 카펫
def solution(brown, yellow):
    grid = brown + yellow
    # n는 세로길이, m 가로길이
    for n in range(3, int(grid ** 0.5) + 1):
        if grid % n == 0:
            m = grid // n
            if yellow == (n - 2) * (m - 2):
                return [m, n]

    return None




# answer = []
#     if yellow == 1:
#         answer.append(3)
#         answer.append(3)
#     for i in range(1, yellow):
#         if yellow % i == 0:
#             temp = yellow // i
#             if brown == ((temp+2)*2 + i*2):
#                 answer.append(temp+2)
#                 answer.append(i+2)
#                 break