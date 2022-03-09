# 코딩테스트 대비 기초 문제 풀이 29일차
# Date : 2022. 02. 15.
# 그리디 문제 풀이

#-------------------------****----------------------------------
# N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계
# N의 범위가 2,000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계
# N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
# N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계
#-------------------------****----------------------------------


# 13432 비서로소 그래프
T = int(input())
 
def gcd(a,b):
    if a<b : a,b = b,a
    if a%b==0:
        return b
    return gcd(b,a%b)
  
for test_case in range(1,T+1):
    print('#'+str(test_case), end = ' ')
    n,s,t = map(int, input().split())
    # 출발점과 목적지가 같으면 이동할 필요 없음
    if s==t:
        print(0)
        continue
    # 1인 경우 무조건 서로소, 서로소인 경우 간선이 없음
    if s==1 or t==1:
        print(-1)
        continue
    # 비서로소인 관계면 간선 하나가 만들어져서 1로 바로 출력 가능
    if gcd(s,t)!=1: 
        print(1)
        continue
  
    lst =[s,t]
    # 2부터(1은 무조건 서로소이기때문) s의 제곱근까지 확인
    for i in range(2,int(s**(1/2))+1):
      # 나누어 진다면 비서로소인 관계이기(간선이 있다) 떄문에 s를 i로 바꿔줌
        if s%i==0:
            lst[0]=i
            break
    # 2부터(1은 무조건 서로소이기때문) s의 제곱근까지 확인
    for i in range(2,int(t**(1/2))+1):
      # 나누어 진다면 비서로소인 관계이기 떄문에 간선이 있다고 간주  t를 i로 바꿔줌
        if t%i==0:
            lst[1]=i
            break
    # 모르겠당
    if lst[0]*lst[1]<=n :
        print(2)
    elif 2*max(lst)<=n:
        print(3)
    else:
        print(-1)