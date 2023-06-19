def solution(N):
    print(bin(N))
    binary = bin(N)[2:]  # N의 이진 표현을 가져오고 '0b' 접두사를 제거합니다
    binary = binary.strip('0')  # 앞뒤로 있는 0을 제거합니다
    gaps = binary.split('1')  # 이진 문자열을 '1'로 분리하여 갭의 목록을 얻습니다
    max_gap = max(len(gap) for gap in gaps) if gaps else 0  # 가장 긴 갭의 길이를 찾습니다

    return max_gap


def intToBinary(n):
    string = ""
    while n != 0:
        string = string + str(n % 2)
        n //= 2
    return string


def solution(N):
    binaryString = intToBinary(N)
    print(binaryString)
    max_gap = 0
    temp_gap = 0
    flag = False
    for i in range(len(binaryString)):
        if binaryString[i] == "1":
            if flag:
                max_gap = max(max_gap, temp_gap)
                temp_gap = 0
            else:
                flag = True
        else:
            temp_gap += 1

    return max_gap