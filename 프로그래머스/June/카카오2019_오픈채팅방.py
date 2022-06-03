def solution(record):
    answer = []
    nickname = dict()
    
    # 닉네임 처리
    for i in record:
        temp = i.split()
        if temp[1] not in nickname.keys():
            nickname[temp[1]] = temp[2]
        else:
            if temp[0] == 'Change' or temp[0] == 'Enter':
                nickname[temp[1]] = temp[2]
        
    # print(nickname)
    for i in record:
        temp = i.split()
        if temp[0] == 'Enter':
            answer.append(f'{nickname[temp[1]]}님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(f'{nickname[temp[1]]}님이 나갔습니다.')
            
    
    return answer