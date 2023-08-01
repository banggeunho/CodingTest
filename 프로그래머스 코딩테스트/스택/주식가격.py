# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 스택 : 어떤 데이터를 넣을건지?, 들어간 데이터는 어떤 의미인지?, 데이터가 나올 때 어떤 상황인지?
def solution(prices):
    n = len(prices)
    answer = [0] * n

    for i in range(n - 1):
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                answer[i] += 1
            # 가격이 내려갈 경우
            else:
                answer[i] += 1
                break

    return answer

def solution(prices):
    n = len(prices)
    stack = []
    answer = [0] * n

    for i in range(n):
        # 가격이 내려갈경우
        while stack and prices[stack[-1]] > prices[i]:
            past = stack.pop()
            answer[past] = i - past

        # 스택에 값 추가
        stack.append(i)

    # 남아있는 스택 비워주기
    for i in stack:
        answer[i] = n - 1 - i

    return answer