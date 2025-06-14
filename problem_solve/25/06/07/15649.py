# https://www.acmicpc.net/problem/15649
# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 예제 입력 1 
# 3 1
# 예제 출력 1 
# 1
# 2
# 3
# 예제 입력 2 
# 4 2
# 예제 출력 2 
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3
# 예제 입력 3 
# 4 4
# 예제 출력 3 
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# 2 4 3 1
# 3 1 2 4
# 3 1 4 2
# 3 2 1 4
# 3 2 4 1
# 3 4 1 2
# 3 4 2 1
# 4 1 2 3
# 4 1 3 2
# 4 2 1 3
# 4 2 3 1
# 4 3 1 2
# 4 3 2 1


"""
1.아이디어
백트래킹 재귀 함수에서 숫자 선택
재귀함수 에서 M개 선택할 경우 프린트

2.시간 복잡도
N!->8! 가능

3. 자료구조
결과값 int[]
방문 여부 체크 bool[]
"""

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs=[]
chk=[False] * (N+1) # 인덱스를 쓰기 위해 0번 인덱스 안쓰려고 N+1 개

def recur(num):
  if num == M:
    print(' '.join(map(str,rs)))
    return
  for i in range(1,N+1):
    if chk[i] == False:
      chk[i] = True
      rs.append(i)
      recur(num+1)
      chk[i] = False
      rs.pop()

recur(0)

N, M = map(int, input().split())

# rs = []
# chk = [False] * (N+1)

# def recur(num):
#     # 1. 함수 호출 시점 로그
#     print(f"recur 호출: num={num}, 현재 수열={rs}, 방문 체크={chk[1:]}")
    
#     # 2. 종료 조건 체크
#     if num == M:
#         print('완성된 수열:', ' '.join(map(str, rs)))
#         return
    
#     # 3. 모든 숫자에 대해 시도
#     for i in range(1, N+1):
#         if chk[i] == False:
#             # 4. 선택 시도 로그
#             print(f"  {i} 선택 시도")
            
#             # 5. 선택하기
#             chk[i] = True
#             rs.append(i)
            
#             # 6. 재귀 호출
#             recur(num+1)
            
#             # 7. 되돌리기 (백트래킹)
#             chk[i] = False
#             rs.pop()
            
#             # 8. 되돌아감 로그
#             print(f"  {i} 선택 취소, 되돌아감")

# recur(0)
