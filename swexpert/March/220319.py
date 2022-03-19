# 코딩테스트 대비 기초 문제 풀이 
# Date : 2022. 03. 19.
# Dynamaic programming
#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****------------------------------------
# 1289 
for tc in range(1, int(input())+1):
  init = input()
  arr = ['0']*len(init)
  cnt = 0
  for i in range(len(init)):
    if arr[i] == '0':
      if arr[i] != init[i]:
        arr[i] = '1'
        cnt += 1
        for j in range(i+1, len(init)):
          arr[j] = '1'
  
    elif arr[i] == '1':
      if arr[i] != init[i]:
        arr[i] = '0'
        cnt += 1
        for j in range(i+1, len(init)):
          arr[j] = '0'
          
    if str(arr) == init:
      break
  print(f'#{tc} {cnt}')


# 1491 ㅇ우워원웑재쟁으의 ㅂ벼벽 ㄲㄲㅜㅁ미믹기
for tc in range(1, int(input())+1):
  n, a, b = map(int, input().split())
  result = 9876543211234
  for r in range(1, n+1):
    for c in range(1, n+1):
      if r*c > n or r < c:
        break
      result = min(result, a*abs(r-c)+b*(n-r*c))
  print(f'#{tc} {result}')



  
    
    
  