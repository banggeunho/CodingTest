class Solution(object):
    def addBinary(self, a, b):
        sumAB = str(int(a) + int(b))
        tmp = list(map(int, sumAB))
        result = ""
        # 두 수를 합한 다음 얘네를 정수형 list로 쪼개줍니다.
        # Carry & Sum
        for i in range(len(tmp) - 1, 0, -1):
            if tmp[i] == 2:
                result = "0" + result
                print(tmp[i - 1])
                tmp[i - 1] += 1

            elif tmp[i] == 3:
                result = "1" + result
                print(tmp[i - 1])
                tmp[i - 1] += 1

            else:
                result = str(tmp[i]) + result

        # 잔챙이 처리
        if tmp[0] == 2:
            result = "10" + result
        elif tmp[0] == 3:
            result = "11" + result
        else:
            result = str(tmp[0]) + result

        print(tmp)
        print(result)
        return result


