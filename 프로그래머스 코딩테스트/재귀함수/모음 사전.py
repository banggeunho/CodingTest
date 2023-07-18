# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# 1. 사전을 만들어 위치 구하기
# 2. 규칙을 찾아서 인덱스로 더하고 빼서 구하기
# 3. 등비 수열로 구하기 등등 ... 시1발
def find(data, p, step):
    if step <= 2:
        print(data, p, step)
    if step == 6:
        return
    if p != '':
        data.append(p)
    for c in ['A', 'E', 'I', 'O', 'U']:
        find(data, ''.join([p, c]), step + 1)

def solution(word):
    data = []
    find(data, "", 0)
    return data.index(word)+1

print(solution("AAAAE"))
# print(solution("AAAE"))

#
# def solution(word):
#     answer = 0
#     arr = ['A', 'E', 'I', 'O', 'U']
#     for a in range(len(arr)):
#         temp = arr[a]
#         answer += 1
#         if temp == word:
#             return answer
#         for b in range(len(arr)):
#             temp = temp[:1]
#             temp += arr[b]
#             answer += 1
#             if temp == word:
#                 return answer
#             for c in range(len(arr)):
#                 temp = temp[:2]
#                 temp += arr[c]
#                 answer += 1
#                 if temp == word:
#                     return answer
#                 for d in range(len(arr)):
#                     temp = temp[:3]
#                     temp += arr[d]
#                     answer += 1
#                     if temp == word:
#                         return answer
#                     for e in range(len(arr)):
#                         temp = temp[:4]
#                         temp += arr[e]
#                         answer += 1
#                         if temp == word:
#                             return answer
#                         # print(temp)
