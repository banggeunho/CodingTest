# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    actions = []
    uid_nick = {}
    for r in record:
        info = r.split()
        cmd, uid = info[0], info[1]
        if cmd in ("Enter", "Change"):
            nickname = info[2]
            uid_nick[uid] = nickname

        actions.append((cmd, uid))

    for cmd, uid in actions:
        if cmd == "Enter":
            answer.append(f'{uid_nick[uid]}님이 들어왔습니다.')
        elif cmd == "Leave":
            answer.append(f'{uid_nick[uid]}님이 나갔습니다.')
        else:
            continue

    return answer