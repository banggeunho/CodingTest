# 완주하지 못한 선수를 체크 해야 함
# 범위는 100,000 < 보통 sort 문제 >
# 둘다 정렬을 했을때 서로 다른게 나온다면 참가자 리턴
# 끝까지 돌렸을떄 나오지 않았다면 마지막 참가자 리턴

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i, j in zip(participant, completion):
        # print(i, j)
        if i != j :
            return i
    return participant[-1]