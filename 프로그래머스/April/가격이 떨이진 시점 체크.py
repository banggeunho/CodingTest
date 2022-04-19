# 가격들의 정보가 주어지고
# 각 가격들이 얼마나 유지하거나 올랐는지 각 배열에 넣어주는 문제
# 순차탐색으로 문제 풀이
# 가격이 떨어지거나 모든 가격을 탐색했을 경우 결과 저장
def solution(prices):
    answer = []
    time = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j] or j == len(prices)-1:
                answer.append(time)
                time = 0
                break

    answer.append(0)
    return answer