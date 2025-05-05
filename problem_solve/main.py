# https://www.acmicpc.net/problem/11724
# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 예제 입력 1 
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 예제 출력 1 
# 2

# 예제 입력 2 
# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3
# 예제 출력 2 
# 1

# 문제 조건에서 M <= N*(N-1)/2 을 준 이유는 NC2 의 경우의 수를 구하기 위함이다. -> 인접 행렬을 사용하는 것이 좋다.

# 체크 배열을 전부 False 로 초기화 해주고, 1부터 N 까지의 정점에 대해 DFS 를 수행한다. DFS 를 수행할 때마다 체크 배열을 True 로 바꿔주고, DFS 가 끝나면 연결 요소의 개수를 1 증가 시킨다. DFS 가 끝난 후 체크 배열을 확인하여 True 인 정점이 있으면 그 정점은 스킵하고 다음 정점으로 넘어간다. 이 과정을 반복하여 모든 정점이 체크 배열에서 True 가 될 때까지 반복한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 제한을 늘려줌

N,M = map(int,input().split())
adj = [[0] * N for _ in range(N)] # 인접 행렬 초기화
for _ in range(M):
   a,b = map(lambda x: x-1, map(int,input().split()))
   adj[a][b] = adj[b][a]= 1

# for row in adj:
#    print(row)
# [0, 1, 0, 0, 1, 0]
# [1, 0, 0, 0, 1, 0]
# [0, 0, 0, 1, 0, 0]
# [0, 0, 1, 0, 0, 1]
# [1, 1, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0]

ans = 0 # 연결 요소의 개수
chk = [False] * N # 체크 배열 초기화

def dfs(now): # DFS 함수 정의
   for nxt in range(N):
      if adj[now][nxt] and not chk[nxt]:
          chk[nxt] = True # 체크 배열을 True 로 바꿔줌
          dfs(nxt)

for i in range(N):
   if not chk[i]:
      ans += 1
      chk[i] = True # 체크 배열을 True 로 바꿔줌
      dfs(i) # DFS 수행
print(ans) # 연결 요소의 개수 출력