# 가능한 경우의 수 담는 list
answer = []

# DFS 함수
def search(begin, target, words, depth):
    global answer
    for word in words:
        if word == target and checkDiff(begin, target): # 현재 단어와 타겟이 하나 차이일 경우
            answer.append(depth)
        
        elif checkDiff(begin, word): # 알파벳 하나 차이 단어 -> begin, words는 현재 단어를 제외하고, depth는 1씩 증가
            search(word, target, [i for i in words if i != begin], depth+1)
            
# 알파벳이 한개 차이가 나는지 아닌지 판별 함수
def checkDiff(query, key):
    diff = 0
    for a,b in zip(query, key):
        if a != b:
            diff += 1 
    return diff == 1     
    
    
def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    search(begin, target, words, 1)
    
    return min(answer)