import math

# 주어진 그림을 활용하여 반복되는 패턴을 찾아 공식을 유추하자.
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))