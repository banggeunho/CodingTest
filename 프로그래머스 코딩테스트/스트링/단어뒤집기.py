# https://www.acmicpc.net/problem/17413
string = input()
answer = ''
open = False
temp_tag = ''
temp_word = ''
for c in string:
    if c in '<>':
        if c == '<':
            if temp_word:
                answer += temp_word[::-1]
                temp_word = ''
            open = True
            temp_tag += c
        elif c == '>':
            open = False
            temp_tag += c
            answer += temp_tag
            temp_tag = ''
    else:
        if open:
            temp_tag += c
        else:
            if c == ' ':
                temp_word = temp_word[::-1] + c
                answer += temp_word
                temp_word = ''
            else:
                temp_word += c

if temp_word != '':
    answer += temp_word[::-1]
print(answer)