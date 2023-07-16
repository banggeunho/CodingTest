# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 내가 만든 버전
def solution(s):
    answer = {}
    strings = s[1:-1].split('},')

    for i in range(len(strings)):
        strings[i] = strings[i].replace('{', '').replace('}', '').split(',')


    strings.sort(key=lambda x:len(x))

    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if int(strings[i][j]) not in answer:
                answer[int(strings[i][j])] = 1

    return list(answer)

# 내가 수정한 버전
def solution(s):
    answer = {}
    strings = s[2:-2].split("},{")

    data = sorted(strings, key=lambda x: len(x))

    for item in data:
        item = list(map(int, item.split(',')))
        for value in item:
            if value not in answer:
                answer[value] = 1

    return list(answer)


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))