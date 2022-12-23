# ord로 먼저 찍어본다...
# print(ord('a'), ord('z')) # 97 122
seq = [i for i in range(97, 123)]
for i in range(1, int(input()) + 1):
    arr = list(input())
    idx = 0
    result = 0
    for j in arr:
        # 문자열 갯수가 seq 범위를 넘어갈 경우 return
        if idx > 25:
            break
        # 문자열으 순서가 seq랑 같으면 count
        if ord(j) == seq[idx]:
            result += 1
        # 순서가 틀려지는 순간 return
        else:
            break
        idx += 1

    print(f'#{i} {result}')
