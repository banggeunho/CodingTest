n = int(input())
count = 0
for _ in range(n):
    string = input()
    chars = [string[0]]
    prev = string[0]
    isNotGroup = False
    for char in string:
        if char not in chars and prev != char: # 이전의 나타나지 않은 값이면 기록
            chars.append(char)

        elif char in chars and prev != char: # 이전의 나타난 값이 나타났을 경우
            isNotGroup = True
            break
            
        prev = char

    if not isNotGroup:
        count += 1

print(count)