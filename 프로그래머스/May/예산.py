def solution(d, budget):
    answer = 0
    for i in sorted(d):
        if budget - i >= 0:
            answer += 1
            budget -= i
        else:
            break
    return answer