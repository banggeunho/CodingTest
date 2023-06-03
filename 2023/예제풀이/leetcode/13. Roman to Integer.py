class Solution(object):
    def romanToInt(self, s):
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # 나올 수 있는 경우의 수를 다 구해서 replace 하는 사람들도 있었음..
        i = 0
        result = 0
        while True:
            if i == len(s):
                break
            print(i, result, s[i])
            if i < len(s) - 1:
                if s[i] == "I":
                    if s[i + 1] in ["V", "X"]:
                        result += romans[s[i + 1]] - romans[s[i]]
                        i += 2
                        continue


                elif s[i] == 'X':
                    if s[i + 1] in ["L", "C"]:
                        result += romans[s[i + 1]] - romans[s[i]]
                        i += 2
                        continue



                elif s[i] == 'C':
                    if s[i + 1] in ["D", "M"]:
                        result += romans[s[i + 1]] - romans[s[i]]
                        i += 2
                        continue

            result += romans[s[i]]
            i += 1

        return result