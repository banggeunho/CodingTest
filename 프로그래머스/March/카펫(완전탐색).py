# 노란색의 모양이 가능한 경우의 수를 하나씩 기준으로 잡았을때
# 예상되는 갈색의 크기와 동일할때 return

def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer.append(3)
        answer.append(3)
    for i in range(1, yellow):
        if yellow % i == 0:
            temp = yellow // i
            if brown == ((temp+2)*2 + i*2):
                answer.append(temp+2)
                answer.append(i+2)
                break

    return answer