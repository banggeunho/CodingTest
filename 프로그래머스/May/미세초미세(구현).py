def currentState(a, b):
    if 151 <= a and 76 <= b: # 마스크 착용 바로 폐기
        return 2

    if 81 <= a or 36 <= b: # 마스크 착용
        return 1


def solution(atmos): # 마스크가 필요한 개수 출력
    answer = 0
    wearingDay = 0
    isMask = 0
    for day, (a, b) in enumerate(atmos):
        if currentState(a, b) == 1:
            if not isMask:
                wearingDay = day
                isMask = 1
                answer += 1 # 마스크 착용 횟수 1회 증가

        if currentState(a, b) == 2:
            if not isMask:
                answer += 1
            isMask = 0

        if wearingDay + 2 == day: # 마스크 폐기
            isMask = 0

    return answer

atmos = [[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]