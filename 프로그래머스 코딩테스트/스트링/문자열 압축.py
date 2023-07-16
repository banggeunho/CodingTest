# https://school.programmers.co.kr/learn/courses/30/lessons/60057#

# n개의 문자로 압축해보고, 가장 길이가 짧은 것을 찾아내어 몇개로 압축했는지 반환해라
# 반복하여 1부터 n-1(문자열의 길이까지) 압축한다.
# 압축할 길이만큼 스트링을 확인한다.

# v1
def solution(s):
    n = len(s)
    answer = len(s)

    for comp_size in range(1, n - 1):
        compressed = ''
        count = 1
        # 이전 문자열과 비교하여
        prev = s[:comp_size]
        for i in range(comp_size, n, comp_size):
            if prev == s[i:i + comp_size]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                count = 1
                prev = s[i:i + comp_size]

        compressed += str(count) + prev if count >= 2 else prev
        print(compressed)
        answer = min(answer, len(compressed))

    return answer

print(solution("a"))