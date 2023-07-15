# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ""
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            continue

        if s[i].isupper():
            if ord(s[i]) + n > ord('Z'):
                answer += chr(ord(s[i]) + n - ord('Z') + ord('A') - 1)
                continue

        if s[i].lower():
            if ord(s[i]) + n > ord('z'):
                answer += chr(ord(s[i]) + n - ord('z') + ord('a') - 1)
                continue

        answer += chr(ord(s[i]) + n)

    return answer