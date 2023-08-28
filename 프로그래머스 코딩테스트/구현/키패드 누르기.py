# https://school.programmers.co.kr/learn/courses/30/lessons/67256

pad = {1: (1, 1), 2: (1, 2), 3: (1, 3),
       4: (2, 1), 5: (2, 2), 6: (2, 3),
       7: (3, 1), 8: (3, 2), 9: (3, 3),
       0: (4, 2)}

def computeDistance(a, b):
    x, y = a
    cx, cy = b
    return abs(x - cx) + abs(y - cy)

def solution(numbers, hand):
    answer = ""
    # hand => left, right
    cur_left = (4, 1)  # *
    cur_right = (4, 3)  # #

    for number in numbers:
        if str(number) in "147":
            answer += 'L'
            cur_left = pad[number]

        elif str(number) in "369":
            answer += 'R'
            cur_right = pad[number]

        else:  # 2580
            if computeDistance(pad[number], cur_left) < computeDistance(pad[number], cur_right):
                answer += 'L'
                cur_left = pad[number]
            elif computeDistance(pad[number], cur_right) < computeDistance(pad[number], cur_left):
                answer += 'R'
                cur_right = pad[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    cur_left = pad[number]
                else:
                    answer += 'R'
                    cur_right = pad[number]

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))





















keypad = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
          '4': (1, 0), '5': (1, 1), '6': (1, 2),
          '7': (2, 0), '8': (2, 1), '9': (2, 2),
          '*': (3, 0), '0': (3, 1), '#': (3, 2)}


def solution(numbers, hand):
    answer = ''
    lx, ly = 3, 0
    rx, ry = 3, 2
    for number in numbers:
        x, y = keypad[str(number)]
        if y == 0:
            answer += 'L'
            lx, ly = x, y

        elif y == 2:
            answer += 'R'
            rx, ry = x, y

        else:
            if abs(x - rx) + abs(y - ry) > abs(x - lx) + abs(y - ly):
                answer += 'L'
                lx, ly = x, y

            elif abs(x - rx) + abs(y - ry) < abs(x - lx) + abs(y - ly):
                answer += 'R'
                rx, ry = x, y

            else:  # 같을 경우
                if hand == 'left':
                    answer += 'L'
                    lx, ly = x, y
                else:
                    answer += 'R'
                    rx, ry = x, y

    return answer