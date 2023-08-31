# https://www.acmicpc.net/problem/3107

bits = input()
bit_list = list(bits.split(':'))
bit_cnt = 0
for bit in bit_list:
    if bit != '':
        bit_cnt += 1
answer = ''
if bits == '::':
    print('0000:0000:0000:0000:0000:0000:0000:0000')

else:
    temp_bit = ''
    blank_cnt = 0
    for c in range(len(bits)):
        if bits[c] == ':':
            if temp_bit:
                zero_len = 4 - len(temp_bit)
                temp_bit = ('0' * zero_len) + temp_bit
                answer += (temp_bit + ':')
                temp_bit = ''

            if c != len(bits)-1 and bits[c+1] == ':': # 연속되어 생략되었을 경우
                answer += '0000:' * (8 - bit_cnt)

        else:
            temp_bit += bits[c]

    if temp_bit:
        zero_len = 4 - len(temp_bit)
        answer += ('0' * zero_len) + temp_bit

print(answer if answer[-1] != ':' else answer[:-1])