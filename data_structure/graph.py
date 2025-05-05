# DFS, BFS, 백트래킹
# 그래프 graph: 노드와 간선으로 이루어진 자료구조
# 각 노드는 vertex, 간선은 edge로 표현
# 노드의 개수는 V, 간선의 개수는 E로 표현

# 무방향(=양방향) 그래프: 간선의 방향이 없는 그래프
# 방향 그래프: 간선의 방향이 있는 그래프

# 순환 그래프: 간선의 방향이 있는 그래프에서, 각 노드가 한 번씩만 방문되는 경로, 즉, 사이클이 존재하는 그래프
# 비순환 그래프: 간선의 방향이 있는 그래프에서, 각 노드가 한 번씩만 방문되는 경로가 없는 그래프, 즉, 사이클이 존재하지 않는 그래프

# 방향 비순환 그래프(DAG): 방향 그래프에서 사이클이 존재하지 않는 그래프
# 예를 들어 깃의 커밋 그래프는 방향 비순환 그래프이다.
# 커밋은 방향 그래프이고, 사이클이 존재하지 않기 때문에 방향 비순환 그래프이다.

# 연결 요소(connected component): 그래프에서 서로 연결된 노드들의 집합
# 연결 그래프: 모든 노드가 서로 연결된 그래프

# 트리 (tree): 사이클이 없는 무방향 그래프
# 가장 바깥쪽 노드는 리프노드
# 리프노드는 자식 노드가 없는 노드
# 노드 개수는 = 간선 개수 + 1
# 노드의 깊이(depth): 루트 노드에서 해당 노드까지의 간선 개수
# 노드의 높이(height): 해당 노드에서 리프 노드까지의 간선 개수
# 노드의 레벨(level): 루트 노드에서 해당 노드까지의 간선 개수 + 1

# 코드로 그래프를 나타내는 방법
# 1. 인접 행렬 (adjacency matrix): 2차원 배열로 그래프를 표현하는 방법, O(V^2)의 공간 복잡도'
# 전부 0으로 초기화하고, 간선이 존재하는 경우 1로 표시
# 예를 들어, 0번 노드와 1번 노드가 연결되어 있다면, adj[0][1] = 1, adj[1][0] = 1로 표시
# 방향 그래프의 경우, adj[0][1] = 1로 표시하고, adj[1][0] = 0으로 표시

# 2. 인접 리스트 (adjacency list): 각 노드에 연결된 노드의 리스트로 그래프를 표현하는 방법, O(E)의 공간 복잡도, 연결 리스트로 구현, 그래도 파이썬에선 리스트로 구현해도 무방
# 각 노드에 연결된 노드의 리스트를 저장하는 배열을 만들고, 각 노드에 연결된 노드를 추가하는 방식으로 구현 
# 예를 들어 0에서 1,2,3으로 가는 간선이 있다면, adj[0] = [1,2,3]으로 표시
# 방향 그래프의 경우, adj[0] = [1,2,3]으로 표시하고, adj[1] = [], adj[2] = [], adj[3] = []으로 표시
# 양방향 그래프의 경우, adj[0] = [1,2,3], adj[1] = [0], adj[2] = [0], adj[3] = [0]으로 표시

# 인접 행렬 VS 인접 리스트
# 인접 행렬: O(V^2)의 공간 복잡도, 간선의 존재 여부를 O(1)로 확인 가능,공간 많이, 시간 적게
# 인접 리스트: O(E)의 공간 복잡도, 간선의 존재 여부를 O(V)로 확인 가능,시간 많이, 공간 적게

# 1. 인접 행렬(Adjacency Matrix) 구현
# 1.1. 무방향 그래프
def create_adj_matrix(vertices, edges):
    matrix = [[0] * vertices for _ in range(vertices)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  # 무방향 그래프이므로 양방향 설정
    return matrix

# 예시: 4개 노드 (0~3)의 무방향 그래프
vertices = 4
edges = [(0,1), (0,2), (0,3), (1,2), (2,3)]
adj_matrix = create_adj_matrix(vertices, edges)

# 출력 결과:
# [
#   [0, 1, 1, 1],
#   [1, 0, 1, 0],
#   [1, 1, 0, 1],
#   [1, 0, 1, 0]
# ]

# 1.2. 방향 그래프
def create_directed_adj_matrix(vertices, edges):
    matrix = [[0] * vertices for _ in range(vertices)]
    for u, v in edges:
        matrix[u][v] = 1  # 단방향만 설정
    return matrix

# 2. 인접 리스트(Adjacency List) 구현
# 2.1. 무방향 그래프
def create_adj_list(vertices, edges):
    graph = {i: [] for i in range(vertices)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # 무방향 그래프이므로 양방향 추가
    return graph

# 예시: 4개 노드 (0~3)의 무방향 그래프
edges = [(0,1), (0,2), (0,3), (1,2), (2,3)]
adj_list = create_adj_list(4, edges)

# 출력 결과:
# {
#   0: [1, 2, 3],
#   1: [0, 2],
#   2: [0, 1, 3],
#   3: [0, 2]
# }

# 2.2. 방향 그래프
def create_directed_adj_list(vertices, edges):
    graph = {i: [] for i in range(vertices)}
    for u, v in edges:
        graph[u].append(v)  # 단방향만 추가
    return graph
