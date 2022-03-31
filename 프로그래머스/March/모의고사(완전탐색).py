def solution(answers):
    answer = []
    first  = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    for i in range(len(answers)):
        if first[i] == answers[i]: cnt1 += 1
        if second[i] == answers[i]: cnt2 += 1
        if third[i] == answers[i]: cnt3 += 1
    
    max_cnt = max(max(cnt1, cnt2), cnt3)
    if max_cnt == cnt1: answer.append(1)
    if max_cnt == cnt2: answer.append(2)
    if max_cnt == cnt3: answer.append(3)

    print(answer)
    return answer