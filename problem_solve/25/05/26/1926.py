# https://www.acmicpc.net/problem/1926

# 문제
# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

# 입력
# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

# 출력
# 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

# 예제 입력 1 
# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1
# 예제 출력 1 
# 4
# 9

"""
1. 아이디어
- 2중 반복문 -> 그래프 값 1 && 방문 안한 경우 DFS
- DFS를 통해 연결된 1의 개수를 세고, 그림의 개수와 넓이를 최대값 갱신

2. 시간 복잡도
- BFS : V = n * m, E = V * 4 (최악의 경우)
- O(V + E) = O(n * m + n * m * 4) = O(n * m)
- O(n * m) = O(250,000) (최악의 경우)

- V: 500 * 500 = 250,000
- E: 250,000 * 4 = 1,000,000 < 2억 : O(n * m) 가능

3. 자료구조
- 그래프: 2차원 리스트 int[][]
- 방문 여부: 2차원 리스트 bool[][]
- DFS 스택: deque
"""

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0  # 그림 개수
max_area = 0  # 최대 넓이

dy = [0,1,0,-1]  # 상하좌우 이동
dx = [1,0,-1,0]

def bfs(y, x):
    area = 1  # 현재 그림의 넓이 (시작점 포함이므로 1부터 시작)
    q = deque()  # BFS 탐색을 위한 큐
    q.append((y, x))  # 시작점을 큐에 추가
    chk[y][x] = True  # 시작점을 방문 처리

    while q:  # 큐가 비어있지 않은 동안 반복
        ey, ex = q.popleft()  # 큐에서 하나의 좌표를 꺼냄
        for k in range(4):  # 상하좌우 4방향 확인
            ny = ey + dy[k]  # 새로운 y 좌표
            nx = ex + dx[k]  # 새로운 x 좌표
            if 0<=ny<n and 0<=nx<m: # 범위 체크
                if map[ny][nx] == 1 and not chk[ny][nx]:  # 1이고 미방문인지 확인
                    area += 1 # 그림 넓이 증가
                    chk[ny][nx] = True # 방문 처리
                    q.append((ny,nx)) # 큐에 추가하여 다음에 탐색
    return area

for j in range(n):
  for i in range(m):
    if map[j][i] == 1 and not chk[j][i]:
      chk[j][i] = True  # 방문 처리
      # 전체 그림 개수 +!
      cnt += 1
      # bfs를 통해 연결된 1의 개수를 세고, 넓이 갱신
      max_area = max(max_area, bfs(j, i))

print(cnt)  # 그림의 개수
print(max_area)  # 최대 넓이