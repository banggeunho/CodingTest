# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 18.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------

# 2806 N-Queens (백트랙킹)
for tc in range(1, int(input())+1):
  n = int(input())
  ans = 0
  row = [0] * n
  
  def is_promising(x):
    # 퀸을 위에서 부터 차례대로 놓는 거라 위에 같은 열 or 같은 대각선 여부만 확인하면 된다.
    for i in range(x):
      if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
        return False

    return True


  def n_queens(x):
    global ans
    if x == n:
      ans += 1
    else:
      for i in range(n):
        row[x] = i
        if is_promising(x):
          n_queens(x+1)

  n_queens(0)
  print(f'#{tc} {ans}')
        
      

# 1860. 진기의 최고급 붕어빵
for tc in range(1, int(input())+1):
  n, m, k = map(int, input().split())
  cus = list(map(int, input().split()))
  cus.sort()
  total, prev, cnt = 0
  solve = True
  for i in cus:
    if i//m >= 1 and i//m != prev:
      cnt += 1
      total = (i//m)*k-cnt
      prev = i//m

    elif total > 0:
      total -= 1
      cnt += 1

    elif i == 0:
      print(f'#{tc} Impossible')
      solve = False
      break
      
    else:
      print(f'#{tc} Impossible')
      solve = False
      break
        
  if solve:
    print(f'#{tc} Possible')
    
    
  
    
    
  