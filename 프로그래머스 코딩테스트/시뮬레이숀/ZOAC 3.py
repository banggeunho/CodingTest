# https://www.acmicpc.net/problem/20436

keyboard = \
    [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
     ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '.'],
     ['z', 'x', 'c', 'v', 'b', 'n', 'm', '.', '.', '.']]

def get_distance(a, b):
    # print(a, b)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_jaum(a):
    if a in 'qwertasdfgzxcv':
        return True
    else:
        return False

keyboard_pos = {}
# ㅋㅣ 위치 저장
for i in range(3):
    for j in range(10):
        keyboard_pos[keyboard[i][j]] = (i, j)

left_hand, right_hand = input().split()

result = input()
answer = 0
for c in result:
    if is_jaum(c):
        answer += get_distance(keyboard_pos[left_hand], keyboard_pos[c])
        left_hand = c

    else:
        answer += get_distance(keyboard_pos[right_hand], keyboard_pos[c])
        right_hand = c

    answer += 1

print(answer)


