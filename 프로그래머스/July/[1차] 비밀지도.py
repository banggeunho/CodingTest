
def num2bit(num, n):
    result = ""

    for i in range(0, n):
        if num % 2 == 1:
            result += '#'
        else:
            result += ' '

        num //= 2

    return result[::-1]

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        result = ""
        t1 = num2bit(a, n)
        t2 = num2bit(b, n)
        for i in range(n):
            if t1[i] == '#' or t2[i] == '#':
                result += "#"
            else:
                result += " "
                
        answer.append(result)
    print(answer)

    return answer