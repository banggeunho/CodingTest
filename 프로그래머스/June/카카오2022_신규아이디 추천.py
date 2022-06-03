def solution(new_id):
    answer = ''
    answer = new_id.lower() # 1단계
    print(answer)
    temp = ''
    for i in answer: # 2단계
        if 'a' <= i <= 'z' or i.isdigit() or i == '-' or i == '_' or i =='.':
            temp += i

    print(temp)
    temp_2 = ''
    point = False # 3단계
    for i in temp:
        if i == '.' and not point:
            point = True
            temp_2 += i
        elif i != '.':
            point = False
            temp_2 += i

    print(temp_2)
    if len(temp_2) >= 1:
        if temp_2[0] == '.': # 4단계
            if len(temp_2) == 1:
                temp_2 = ''
            else:
                temp_2 = temp_2[1:]
        
        if len(temp_2) > 1:
            if temp_2[-1] == '.':
                temp_2 = temp_2[:-1]

    print(temp_2)
    if len(temp_2) >= 16: # 6단계
        temp_2 = temp_2[:15]
        if temp_2[-1] == '.':
            temp_2 = temp_2[:-1]
            
    if len(temp_2) == 0: # 5단계
        temp_2 = 'a'

    answer = temp_2
    if len(temp_2) <= 2: # 7단계
        while True:
            answer += temp_2[-1]
            if len(answer) >= 3:
                break

    print(answer)
    return answer