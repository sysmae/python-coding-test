# https://www.acmicpc.net/problem/17136

# 문제
# <그림 1>과 같이 정사각형 모양을 한 다섯 종류의 색종이가 있다. 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.

# https://upload.acmicpc.net/496452ae-ce36-4d77-93f7-19d7f3f9ce28/-/preview/

# <그림 1>

# 색종이를 크기가 10×10인 종이 위에 붙이려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다. 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.

# 종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.

# 입력
# 총 10개의 줄에 종이의 각 칸에 적힌 수가 주어진다.

# 출력
# 모든 1을 덮는데 필요한 색종이의 최소 개수를 출력한다. 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다.

# 예제 입력 1 
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 예제 출력 1 
# 0
# 예제 입력 2 
# 0 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 예제 출력 2 
# 4
# 예제 입력 3 
# 0 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 예제 출력 3 
# 5
# 예제 입력 4 
# 0 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 예제 출력 4 
# -1
# 예제 입력 5 
# 0 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 0 0 0 0
# 0 1 1 1 0 0 0 0 0 0
# 0 0 1 1 1 1 1 0 0 0
# 0 0 0 1 1 1 1 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 예제 출력 5 
# 7
# 예제 입력 6 
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 예제 출력 6 
# 4
# 예제 입력 7 
# 0 0 0 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0 0 0 0
# 0 1 1 1 1 1 0 0 0 0
# 0 0 1 1 1 1 0 0 0 0
# 0 0 1 1 1 1 0 0 0 0
# 0 1 1 1 1 1 1 1 1 1
# 0 1 1 1 0 1 1 1 1 1
# 0 1 1 1 0 1 1 1 1 1
# 0 0 0 0 0 1 1 1 1 1
# 0 0 0 0 0 1 1 1 1 1
# 예제 출력 7 
# 6
# 예제 입력 8 
# 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 0 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0
# 0 1 1 1 0 1 1 0 0 0
# 0 1 1 1 0 1 1 0 0 0
# 0 1 1 1 0 0 0 0 0 1
# 예제 출력 8 
# 5

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)] 
ans = 1e9 # 최대치는 25개 색종이로 덮는 것
paper = [0] * 6 # 사용한 색종이 개수 크기 1~5


def is_possible(y,x,size):
  # 색종이 갯수 체크
  if paper[size] == 5:
    return False
  # 범위 체크
  if y + size > 10 or x + size > 10:
    return False
  # 색종이 붙일 수 있는지 체크
  for i in range(size):
    for j in range(size):
      if board[y+i][x+j] == 0:
        return False
  return True

def mark(y,x,size,v):
  for i in range(size):
    for j in range(size):
      board[y+i][x+j] = v
  
  if v:
    paper[size] -= 1
  else:
    paper[size] += 1

def backtracking(y,x):
  global ans
  if y==10:
    ans = min(ans, sum(paper))
    return
  if x==10:
    backtracking(y+1,0)
    return
  if board[y][x] == 0:
    backtracking(y,x+1)
    return
  
  for size in range(1,6):
    if is_possible(y,x,size):
      # 색종이 붙이기
      mark(y,x,size,0)
      backtracking(y,x+1)
      # 색종이 원상복구
      mark(y,x,size,1) # 원상복구

backtracking(0,0)
print(ans if ans != 1e9 else -1)


# def backtracking(y,x):
#     global ans
#     if x == 10: # 다음 줄로 넘어감
#         y += 1
#         x = 0
#     if y == 10: # 모든 칸을 다 확인했으면
#         ans = min(ans, sum(paper[1:])) # 색종이 개수의 최솟값을 갱신
#         return

#     if board[y][x] == 1: # 색종이를 붙일 수 있는 경우
#         for size in range(5,0,-1): # 큰 색종이부터 붙여보자
#             if paper[size] < 5: # 색종이가 남아있다면
#                 flag = True
#                 for i in range(size):
#                     for j in range(size):
#                         if y+i >= 10 or x+j >= 10 or board[y+i][x+j] != 1:
#                             flag = False
#                             break
#                     if not flag:
#                         break

#                 if flag: # 색종이를 붙일 수 있다면
#                     for i in range(size):
#                         for j in range(size):
#                             board[y+i][x+j] = 0 # 색종이를 붙인다.
#                     paper[size] += 1 # 사용한 색종이 개수 증가
#                     backtracking(y,x+1) # 다음 칸으로 이동
#                     paper[size] -= 1 # 사용한 색종이 개수 감소
#                     for i in range(size):
#                         for j in range(size):
#                             board[y+i][x+j] = 1 # 색종이를 다시 원래대로 돌린다.
#     else:
#         backtracking(y,x+1) # 다음 칸으로 이동
  