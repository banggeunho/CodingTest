import math
import itertools
def isPrime(num): # 소수 판별 함수
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    arr = list(numbers) # 스트링 -> 리스트
    for k in range(1, len(arr)+1):
        cases = itertools.permutations(arr, k) # 모든 경우의 수 뽑기
        for case in cases: # 각 경우 마다 뽑힌 숫자들을 합친 후 정수형으로 변환
            temp = int(''.join(case))
            if isPrime(temp): # 소수이면서, 기존에 추가되지 않은 정수면 정답 list에 추가
                if temp not in answer:
                    answer.append(temp)

    print(answer)
    return len(answer)

solution("011")