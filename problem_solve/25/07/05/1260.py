"""
https://www.acmicpc.net/problem/1260
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1
1 2 4 3
1 2 3 4
예제 입력 2
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2
3 1 2 5 4
3 1 4 2 5
예제 입력 3
1000 1 1000
999 1000
예제 출력 3
1000 999
1000 999
"""

import sys
from collections import deque

input = sys.stdin.readline


N, M, V = map(int, input().split())
# 인접 리스트로 그래프를 표현
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # 간선의 양 끝점을 입력받아 그래프에 추가
    a, b = map(int, input().split())
    # 양방향 그래프이므로 양쪽 모두에 간선을 추가
    graph[a].append(b)
    graph[b].append(a)
# 각 정점의 인접 리스트를 정렬하여 작은 번호부터 방문하도록 함
for i in range(1, N + 1):
    graph[i].sort()
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dq = deque()


def dfs(v):
    visited_dfs[v] = True  # 현재 노드 방문 표시
    print(v, end=" ")  # 현재 노드 출력
    for i in graph[v]:  # 현재 노드와 연결된 모든 노드에 대해
        if not visited_dfs[i]:
            dfs(i)  # 방문하지 않은 노드가 있다면 재귀적으로 DFS 호출


def bfs(v):
    dq.append(V)  # 시작 노드를 큐에 추가
    visited_bfs[v] = True  # 시작 노드 방문 표시
    while dq:
        v = dq.popleft()  # 큐에서 노드를 꺼냄
        print(v, end=" ")  # 꺼낸 노드 출력
        for i in graph[v]:
            if not visited_bfs[i]:
                dq.append(i)  # 방문하지 않은 노드를 큐에 추가
                visited_bfs[i] = True  # 해당 노드 방문 표시


# DFS 탐색 시작
dfs(V)
print()  # DFS와 BFS 결과를 구분하기 위한 줄바꿈
# BFS 탐색 시작
bfs(V)
