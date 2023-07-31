# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    clothes_dict = {}

    for name, type in clothes:
        clothes_dict[type] = clothes_dict.get(type, 0) + 1


    for type in clothes_dict:
        answer *= (clothes_dict[type] + 1)

    # 모든 옷을 입지 않을 경우는 제외
    return answer - 1