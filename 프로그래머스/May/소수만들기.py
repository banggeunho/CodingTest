import math
import itertools

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    cases = itertools.combinations(nums, 3)
    for case in cases:
        if isPrime(sum(case)):
            answer += 1

    return answer