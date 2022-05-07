def solution(n, words):
    answer = []
    save = [words[0]]
    prev = words[0]
    for i in range(1, len(words)):
        if prev[-1] != words[i][0]: # 앞 뒤 글자가 다를 경우
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
        
        if words[i] in save: # 이미 등장한 단어
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
            
        prev = words[i]
        save.append(words[i])
        
    if not answer:
        return [0, 0]

    return answer