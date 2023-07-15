# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    # s를 공백문자로 스플릿 한다.
    strings = list(s)
    cnt = 0
    # 각 단어들을 탐색하며, 짝수 -> 대문자, 홀수 -> 소문자로 문자열을 바꿔준다.
    for i in range(len(strings)):

        if strings[i] == ' ':
            cnt = 0
            answer += ' '
            continue

        answer += strings[i].upper() if cnt % 2 == 0 else strings[i].lower()
        cnt += 1

    # 다시 조인해서 리턴한다.
    return answer