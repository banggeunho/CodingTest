def solution(s):
    answer = ''
    
    table = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for i in range(len(s)):
        if s[i].isdigit():
            answer += str(s[i])
        
        else:
            temp = s[i]
            for j in range(i+1, len(s)):
                temp += s[j]
                if temp in table.keys():
                    answer += str(table[temp])
                    break
            
    return int(answer)