#https://programmers.co.kr/learn/courses/30/lessons/42578
# 옷의 종류와 그에 대응하는 숫자만 뽑아내서
# 조합을 계산한다(옷의개수 + 안입은 경우(1)로 해서 구해준다.)
# 모든 옷을 안입었을 경우가 있으므로 최종적으로 -1을 해준다.
def solution(clothes):
    clothes_type = {}
    for _, j in clothes:
        if j not in clothes_type:
            clothes_type[j] = 1
        elif j in clothes_type:
            clothes_type[j] += 1
    print(clothes_type)
    answer = 1
    for i in list(clothes_type.values()):
        answer *= i+1

    return answer-1