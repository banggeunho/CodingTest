string = input()
bomb = input()
m = len(bomb)

stack = []
for i in string:
    stack.append(i)
    if i == bomb[-1] and ''.join(stack[-m:]) == bomb:
        del stack[-m:]

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
