
# BFS 너비 우선 탐색
# 큐를 사용하여 구현
# 시작 노드에서 인접한 노드를 모두 방문하고, 그 다음 인접한 노드를 방문하는 방식으로 탐색

from collections import deque

adjacency_matrix = [[0] * 13 for _ in range(13)]
adjacency_matrix[0][1] = adjacency_matrix[0][2]= 1
adjacency_matrix[1][3] = adjacency_matrix[1][4]= 1

def bfs():
  dq = deque()
  dq.append(0) # 시작 노드
  while dq:
    now = dq.popleft()
    print(now, end=' ')
    for nxt in range(13):
      if adjacency_matrix[now][nxt]:
        dq.append(nxt)

bfs()
# Output: 0 1 2 3 4

# DFS 깊이 우선 탐색
# 스택 or 재귀로 구현

# 인접 행렬로 그래프를 표현
adjacency_matrix = [[0] * 13 for _ in range(13)]
adjacency_matrix[0][1] = adjacency_matrix[0][7]= 1
adjacency_matrix[1][2] = adjacency_matrix[1][5]= 1
# print(adjacency_matrix)

visited = [False] * 13  # Initialize visited list for 13 nodes

def dfs(now):
    for nxt in range(13):
        if adjacency_matrix[now][nxt] == 1 and not visited[nxt]:
            visited[nxt] = True
            print(nxt, end=' ')
            dfs(nxt)


# BFS와 DFS의 차이점
# BFS는 큐를 사용하여 인접한 노드를 모두 방문하고, 그 다음 인접한 노드를 방문하는 방식으로 탐색
# DFS는 스택을 사용하여 깊이 우선으로 탐색하는 방식으로, 재귀를 사용하여 구현할 수 있음

# 예컨대 최단 거리 탐색을 할 때는 BFS를 사용하면 좋고, 경로 탐색을 할 때는 DFS를 사용하면 좋음

# 시간 복잡도
# 인접 행렬로 그래프를 표현할 때
# BFS: O(V^2) (V: 노드 수)
# DFS: O(V^2) (V: 노드 수)

# 인접 리스트로 그래프를 표현할 때
# BFS: O(V + E) (V: 노드 수, E: 간선 수)
# DFS: O(V + E) (V: 노드 수, E: 간선 수)

# 공간 복잡도
# 인접 행렬로 그래프를 표현할 때
# BFS: O(V^2) (V: 노드 수)
# DFS: O(V^2) (V: 노드 수)

# 인접 리스트로 그래프를 표현할 때
# BFS: O(V + E) (V: 노드 수, E: 간선 수)
# DFS: O(V + E) (V: 노드 수, E: 간선 수)

# 참고: 인접 리스트로 그래프를 표현
# adjacency_list = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# 길찾기 문제 예시코드
dy = (0,1,0,-1) # 상하좌우
dx = (1,0,-1,0) # 상하좌우
chk = [[False] * 100 for _ in range(100)] # 100x100 맵
N = int(input()) # 맵 크기

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N and not chk[y][x] # 맵의 범위 안에 있고, 방문하지 않은 좌표인지 확인

def bfs(start_y, start_x):
    dq = deque()
    dq.append((start_y, start_x)) # 시작 좌표
    chk[start_y][start_x] = True # 시작 좌표 방문 처리
    while len(dq)>0:
        now_y, now_x = dq.popleft() # 현재 좌표
        for i in range(4): # 상하좌우 탐색
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]
            if is_valid_coord(next_y, next_x): # 유효한 좌표인지 확인
                chk[next_y][next_x] = True # 방문 처리
                dq.append((next_y, next_x)) # 큐에 추가