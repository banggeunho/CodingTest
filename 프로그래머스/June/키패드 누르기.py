keypad = {'1': (0, 0), '2':(0, 1), '3':(0,2),
          '4': (1, 0), '5':(1, 1), '6':(1, 2),
          '7': (2, 0), '8':(2, 1), '9': (2, 2),
          '*': (3, 0), '0':(3, 1), '#':(3,2)}

def solution(numbers, hand):
    answer = ''
    lx, ly = 3, 0 # 초기 왼손 위치
    rx, ry = 3, 2 # 초기 오른손 위치
    for number in numbers:
        x, y = keypad[str(number)] # 키패드 위치 가져오기
        if y == 0: # 왼쪽 열이면 모두 왼손으로 처리
            answer += 'L'
            lx, ly = x, y
        
        elif y == 2: # 오른쪽 열이면 모두 오른손으로 처리
            answer += 'R'
            rx, ry = x, y
        
        else: # 가운데 열일 경우 거리를 비교하여 처리 (가까운 거리에 위치한 손 사용)
            if abs(x - rx) + abs(y - ry) > abs(x - lx) + abs(y - ly):
                answer += 'L'
                lx, ly = x, y
            
            elif abs(x - rx) + abs(y - ry) < abs(x - lx) + abs(y - ly):
                answer += 'R'
                rx, ry = x, y
                
            else: # 거리가 같을 경우
                if hand == 'left':
                    answer += 'L'
                    lx, ly = x, y
                else:
                    answer += 'R'
                    rx, ry = x, y
                
    return answer