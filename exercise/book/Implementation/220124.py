# 코딩테스트 대비 기초 문제 풀이 6일차
# Date : 2022. 01. 24.
# 구현(Implementation)에 관한 기초 문제 풀이


# 왕실의 나이트 (예제 4-2)
# 나이트는 8X8 형태의 좌표평면위에서 L자형태로만 이동가능하다.
# 1. 수평으로 두 칸 이동한 뒤에 수직을 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 행 위치를 표현할 때는 1부터 8로 표현하여, 열 위치를 표현할 때는 A부터 H로 나타냄.


n = input()

# col은 알파벳으로 입력 받기 때문에, ASCII CODE로 변환하여 정수로 캐스팅한다.
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1 

# 이동할 수 있는 모든 경우의 수
steps = [(2,1), (2,-1), (-2, 1), (-2, -1), (-1, 2), (1, 2), (1,-2), (-1, -2)]

count = 0
# 이동할 수 있는 모든 경우의 수 중에 이동했을때 8*8 안에 있는 것만 세어주면 된다.
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]

  # 정원의 사이즈에 만족할 때 카운트 적립
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    count += 1

# 최종 결과 출력
print(count)
