n = int(input())

result = ""

roman = {1:"I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX",  40: "XL", 90: "XC", 400: "CD", 900: "CM"}
roman_val = sorted(list(roman.keys()), reverse=True)
i=0
while n > 0:
    while n >= roman_val[i]:
            n -= roman_val[i]
            result += roman[roman_val[i]]
    i += 1

print(result)

