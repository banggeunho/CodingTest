# 잣같이 풀었다... 나중에 다시 풀어보자.....슈발....
import copy
answer = []
def dfs(path, dest, tickets):
    temp = copy.deepcopy(path)
    temp1 = copy.deepcopy(tickets)
    temp.append(dest)
    cnt = 0
    if len(tickets) < 1:
        answer.append(temp)
        return

    for ticket in tickets:
        if dest == ticket[0]:
            temp1.remove([ticket[0], ticket[1]])
            dfs(temp, ticket[1], temp1)
            temp1.append([ticket[0], ticket[1]])
            cnt += 1

    if cnt == 0:
        return

def solution(tickets):
    global answer, length, city
    answer = []
    temp = copy.deepcopy(tickets)
    for ticket in tickets:
        if ticket[0] == "ICN":
            temp.remove([ticket[0], ticket[1]])
            dfs(['ICN'], ticket[1], temp)
            temp.append([ticket[0], ticket[1]])

    answer.sort()
    return answer[0]