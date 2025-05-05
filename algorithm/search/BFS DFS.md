## 그래프 표현 방법

**인접 행렬 (Adjacency Matrix)**  
– V개의 노드가 있을 때 V×V 크기의 2차원 배열로 간선을 표현  
– 연결 여부만 체크할 때 간단하지만, 노드 수가 많아지면 메모리 낭비 발생

```python
# 인접 행렬 예시
adjacency_matrix = [[0] * 13 for _ in range(13)]
adjacency_matrix[0][1] = adjacency_matrix[0][2]= 1
adjacency_matrix[1][3] = adjacency_matrix[1][4]= 1
```

**인접 리스트 (Adjacency List)**  
– 각 노드가 연결된 이웃 노드 리스트를 갖는 구조  
– 간선 수 E에 비례해 메모리를 사용하므로 희소 그래프에서 유리

```python
# 인접 리스트 예시
adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

## BFS (너비 우선 탐색)

– **원리**: 큐(Queue)를 이용해 시작 노드와 같은 단계에 있는 모든 노드를 먼저 방문  
– **특징**: 최단 경로 탐색에 적합

```python
from collections import deque

def bfs(adj_matrix, start=0):
    V = len(adj_matrix)
    visited = [False] * V
    dq = deque([start])
    visited[start] = True

    while dq:
        now = dq.popleft()
        print(now, end=' ')
        for nxt in range(V):
            if adj_matrix[now][nxt] and not visited[nxt]:
                visited[nxt] = True
                dq.append(nxt)

# 사용 예시
adj_matrix = [[0]*5 for _ in range(5)]
adj_matrix[0][1] = adj_matrix[0][2] = 1
adj_matrix[1][3] = adj_matrix[1][4] = 1
bfs(adj_matrix, 0)  # 출력: 0 1 2 3 4
```

## DFS (깊이 우선 탐색)

– **원리**: 스택(Stack) 또는 재귀를 이용해 한 방향으로 최대한 깊이 내려간 뒤, 더 이상 갈 곳이 없으면 되돌아오며 탐색  
– **특징**: 경로 존재 여부 탐색에 유리, 구현이 간결

```python
def dfs(adj_matrix, now, visited):
    print(now, end=' ')
    for nxt in range(len(adj_matrix)):
        if adj_matrix[now][nxt] and not visited[nxt]:
            visited[nxt] = True
            dfs(adj_matrix, nxt, visited)

# 사용 예시
adj_matrix = [[0]*5 for _ in range(5)]
adj_matrix[0][1] = adj_matrix[0][7%5] = 1  # 예시용
adj_matrix[1][2] = adj_matrix[1][5%5] = 1
visited = [False]*5
visited[0] = True
dfs(adj_matrix, 0, visited)
```

## 시간·공간 복잡도 비교

| 그래프 표현 | 알고리즘 | 시간 복잡도 | 공간 복잡도 |
| ----------- | -------- | ----------- | ----------- |
| 인접 행렬   | BFS      | O(V²)       | O(V²)       |
| 인접 행렬   | DFS      | O(V²)       | O(V²)       |
| 인접 리스트 | BFS      | O(V + E)    | O(V + E)    |
| 인접 리스트 | DFS      | O(V + E)    | O(V + E)    |

## 미로 탐색 예제 (격자 기반 길찾기)

상하좌우 네 방향으로 이동하며, BFS를 통해 최단 경로를 찾는 예제입니다.

```python
from collections import deque

# 이동 방향 (우, 하, 좌, 상)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def is_valid_coord(y, x, N, visited):
    return 0 <= y < N and 0 <= x < N and not visited[y][x]

def bfs_maze(maze, start, end):
    N = len(maze)
    visited = [[False]*N for _ in range(N)]
    dq = deque([(start[0], start[1], 0)])  # y, x, distance
    visited[start[0]][start[1]] = True

    while dq:
        y, x, dist = dq.popleft()
        if (y, x) == end:
            return dist
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if is_valid_coord(ny, nx, N, visited) and maze[ny][nx] == 0:
                visited[ny][nx] = True
                dq.append((ny, nx, dist+1))
    return -1  # 경로가 없을 때

# 사용 예시
maze = [
    [0,1,0,0],
    [0,1,0,1],
    [0,0,0,1],
    [1,0,1,0],
]
print(bfs_maze(maze, (0,0), (3,3)))  # 최단 거리 출력
```

## 활용 팁

- BFS로 최단 경로 길이를 구하거나 레벨별 탐색이 필요할 때 사용.
- DFS로 경로 존재 여부 확인, 순열 조합 생성, 백트래킹 문제 해결에 적합.
- 메모리 절약이 필요하면 인접 리스트, 빠른 접근이 중요하면 인접 행렬로 그래프 표현 방식을 선택.
- 재귀 깊이 한계가 있는 환경에서는 DFS를 스택 기반으로 구현하거나, 파이썬의 재귀 한계를 늘리는 방법 고려.

이 한 권의 핸드북으로 그래프 탐색의 기본 개념부터 구현, 복잡도 분석, 실제 응용 예제까지 손쉽게 참고할 수 있습니다. 다양한 문제에 맞춰 적절한 탐색 알고리즘을 선택해 보세요.

---

Perplexity로부터의 답변: pplx.ai/share
