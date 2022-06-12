# 문자해독 1593
# itertools 을 사용해서 풀이 -> 시간초과
# sorting과 슬라이딩을 사용해서 풀이 -> 시간초과
# 입력된 문자열의 각 문자를 count 해서 마야 문자열을 슬라이딩해서 같은 갯수를 갖고 있는지 확인해야 하는 문제
g, l = map(int, input().split())
w = list(input())
arr = list(input())

w_l = [0]*52
s_l = [0]*52

for word in w:
    if 'a' <= word <= 'z': # 소문자일 경우
        w_l[ord(word)-ord('a')] += 1
    else:
        w_l[ord(word)-ord('A')+26] += 1

length, answer, start = 0, 0, 0 # 현재까지 본 길이, 정답 카운트, 현재 슬라이드 시작 지점
for i in range(l):
    if 'a' <= arr[i] <= 'z':
        s_l[ord(arr[i]) - ord('a')] += 1
    else:
        s_l[ord(arr[i]) - ord('A') + 26] += 1
    length += 1

    if length == g: # 입력된 비교할 문자열의 길이만큼 정보가 담겼을때
        if w_l == s_l:
            answer += 1
        if 'a' <= arr[start] <= 'z':
            s_l[ord(arr[start]) - ord('a')] -= 1
        else:
            s_l[ord(arr[start]) - ord('A') + 26] -= 1
        start += 1 # 한 칸씩 슬라이딩
        length -= 1 # 슬라이딩 햇으니 length 하나 줄여준다.

print(answer)

