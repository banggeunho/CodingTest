# https://school.programmers.co.kr/learn/courses/30/lessons/67258
def solution(gems):
    answer = [1, int(1e9)]
    uGems = set(gems)

    for i in range(len(gems)):
        tempSet = set()
        tempSet.add(gems[i])
        if tempSet == uGems:
            answer[0] = i + 1
            answer[1] = i + 1
            break

        for j in range(i + 1, len(gems)):
            tempSet.add(gems[j])

            if tempSet == uGems and (answer[1] - answer[0]) > (j - i):
                answer[0] = i + 1
                answer[1] = j + 1
                break

    return answer


def solution(gems):
    answer = []
    kind = len(set(gems))
    size = len(gems)
    answer = [0, size - 1]

    dic = {gems[0]: 1}
    start = end = 0
    # 즉, 보석의 한 종류 이상 가졌을 경우 맨 앞의 보석을 팔고 그걸 기준으로 다시 탐색 진행하면서 최소 구간을 찾기
    while end < size:  # 전체 보석을 탐색
        if len(dic) < kind:  # 즉, 보석 한 종류 이상 가지지 못했을 경우
            end += 1
            if end == size: break  # 가졌으면 break
            dic[gems[end]] = dic.get(gems[end], 0) + 1  # 아니면 종류를 채워 넣는다.
        else:  # 보석을 다 채웠을 경우
            if (end - start + 1) < (answer[1] - answer[0] + 1): answer = [start, end]  # 값을 비교하여 갱신
            if dic[gems[start]] == 1:
                del dic[gems[start]]  # start 지점의 보석이 이미 있으면 지워줌
            else:
                dic[gems[start]] -= 1  # 1이 아니면 1을 빼준다.
            start += 1

    answer[0] += 1
    answer[1] += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))