"""
https://www.acmicpc.net/problem/1697
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1
5 17
예제 출력 1
4
힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
"""

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

dq = deque()
visited = [False] * 100001


# BFS를 사용하여 최단 경로를 찾는 문제
# 수빈이의 위치 N과 동생의 위치 K를 입력받아 최단 시간을 계산하는 함수
def bfs(start, target):
    dq.append((start, 0))  # (현재 위치, 시간)
    visited[start] = True  # 시작 위치 방문 처리
    while dq:
        current, time = dq.popleft()  # 현재 위치와 시간을 꺼냄
        if current == target:  # 현재 위치가 동생의 위치와 같으면
            return time  # 시간을 반환
        # 다음 위치를 계산
        next_positions = [current - 1, current + 1, 2 * current]
        for next_pos in next_positions:
            if (
                0 <= next_pos <= 100000 and not visited[next_pos]
            ):  # 범위 내에 있고 방문하지 않은 위치
                visited[next_pos] = True  # 방문 처리
                dq.append((next_pos, time + 1))  # 다음 위치와 시간을 큐에 추가


# BFS를 호출하여 최단 시간을 계산하고 출력
print(bfs(N, K))
