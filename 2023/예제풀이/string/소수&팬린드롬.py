#https://www.acmicpc.net/problem/1747
import math
def isPanlindrome(n):
    string = str(n)
    return string == string[::-1]

def isPrimeNum(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

n = int(input())
while True:
    if isPanlindrome(n):
        if isPrimeNum(n):
            print(n)
            break

    n += 1

