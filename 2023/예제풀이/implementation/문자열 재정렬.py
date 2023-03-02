
data = list(input())
char_sum = []
num_sum = 0
for char in data:
    if char.isalpha():
        char_sum.append(char)
    else:
        num_sum += int(char)

char_sum.sort()

if num_sum != 0: # 숫자가 하나라도 존재할 경우 맨 뒤에 삽입
    char_sum.append(str(num_sum))

print(''.join(char_sum))



