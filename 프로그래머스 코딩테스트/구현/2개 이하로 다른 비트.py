# https://school.programmers.co.kr/learn/courses/30/lessons/77885
def f(x):
    # 짝수면 1 더한게 최솟값
    if x % 2 == 0: return x + 1

    # 홀수면 처음 나오는 0의 자리를 10으로 바꿔주면 된다.
    x = f'0{bin(x)[2:]}'
    x = f"{x[:x.rindex('0')]}10{x[x.rindex('0') + 2:]}"
    return int(x, 2)


def solution(numbers):
    return [f(number) for number in numbers]


print(solution([3, 5, 7, 9, 11]))