# 폭탄의 끝 문자와 입력된 문자가 같은경우 확인해봐라
# 폭탄의 길이만큼 스택의 뒷부분을 가져왔을때 같으면 터트려라
# 이런식으로 작성하면 연쇄 폭파 가능
# 지울떄는 del 함수를 이용 가능


data = input()
bomb = input()
idx = len(bomb)

stack = []
for i in data:
    stack.append(i)
    if i == bomb[-1] and ''.join(stack[-idx:]) == bomb:
        del stack[-idx:]

if len(stack) == 0: print('FRULA')
else: print(''.join(stack))