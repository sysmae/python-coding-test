# https://www.acmicpc.net/problem/2667
# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# 예제 입력 1 
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# 예제 출력 1 
# 3
# 7
# 8
# 9

"""
아이디어 
이중 for 문을 통해 1을 찾으면 dfs를 통해 연결된 집의 개수를 세고, 단지 수를 증가시킨다.

시간 복잡도
DFS : O(V + E)
V,E : V = N^2, E = 4V (최악의 경우 모든 노드가 연결되어 있을 때)
V+E = O(N^2) ->  5≤N≤25 dfs는 최대 625번 호출됨

자료구조
그래프 저장: 2차원 리스트
방문 방문 여부: 2차원 리스트
결과값 : 리스트

"""

import sys

input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
  global each
  each +=1
  for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]
    if 0 <= ny < N and 0 <= nx <N: 
      if map[ny][nx] == 1 and chk[ny][nx] == False:
        chk[ny][nx] = True
        dfs(ny,nx)


for j in range(N):
  for i in range(N):
    if map[j][i] == 1 and chk[j][i] == False:
    # 방문 체크 표시
      chk[j][i] = True
    # DFS 로 크기 구하기
      each = 0
      dfs(j,i)
    # 크기를 결과 리스트에 넣기
      result.append(each)

result.sort()

print(len(result))
for i in result:
  print(i)