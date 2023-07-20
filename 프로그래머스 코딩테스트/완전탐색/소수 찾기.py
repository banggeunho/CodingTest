import math
from itertools import permutations

def isPrimeNum(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        cases = list(permutations(list(numbers), i))
        for case in cases:
            num = int(''.join(case))
            if isPrimeNum(num):
                answer.add(num)

    return len(answer)

print(solution("011"))


def solution(numbers):
    numbers = list(numbers)
    answer = []

    for i in range(1, len(numbers) + 1):
        answer.append(list(permutations(numbers, i)))

    answer = [int(''.join(y)) for x in answer for y in x if isPrimeNum(int(''.join(y)))]

    return len(set(answer))




















#
# import math
# import itertools
# def isPrime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def solution(numbers):
#     answer = []
#     arr = list(numbers)
#     for k in range(1, len(arr)+1):
#         cases = itertools.permutations(arr, k)
#         for case in cases:
#             temp = int(''.join(case))
#             if isPrime(temp):
#                 if temp not in answer:
#                     answer.append(temp)
#
#     print(answer)
#     return len(answer)