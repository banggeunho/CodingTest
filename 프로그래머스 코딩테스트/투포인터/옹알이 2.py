# https://school.programmers.co.kr/learn/courses/30/lessons/133499
def solution(babbling):
    answer = 0
    can_speaks = set(["aya", "ye", "woo", "ma"])
    for bab in babbling:
        start = 0
        # print("새단어시작")
        while start < len(bab) - 1:
            prev = ""
            temp = bab[start]
            for j in range(start + 1, len(bab)):
                # print(temp, prev, start)
                temp += bab[j]
                if temp in can_speaks and prev != temp:
                    prev = temp
                    temp = ""
                    start = j + 1

            if temp == "":
                answer += 1
            break

    return answer