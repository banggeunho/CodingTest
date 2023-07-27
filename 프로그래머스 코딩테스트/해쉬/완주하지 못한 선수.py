
def solution(participant, completion):
    answer = {}
    for i in participant:
        answer[i] = answer.get(i, 0) + 1

    for j in completion:
        answer[j] -= 1

    for k in answer:
        if answer[k]:
            return k


def solution(participant, completion):
    value = 0
    answer = {}

    for i in participant:
        hash_value = int(hash(i))
        answer[hash_value] = i
        value += hash_value

    for j in completion:
        hash_value = int(hash(j))
        value -= hash_value

    return answer[value]

