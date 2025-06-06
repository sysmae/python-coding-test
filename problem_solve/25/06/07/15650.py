# https://www.acmicpc.net/problem/15650
# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
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
# 2 3
# 2 4
# 3 4
# 예제 입력 3 
# 4 4
# 예제 출력 3 
# 1 2 3 4
# 출처

# 백트래킹으로 조합을 구하는 문제입니다.
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
def backtrack(start, path):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N + 1):
        backtrack(i + 1, path + [i])

backtrack(1, [])


# import sys
# input = sys.stdin.readline

# # N: 1부터 N까지의 자연수 범위
# # M: 선택할 수의 개수
# N, M = map(int, input().split())

# def backtrack(start, path):
#     """
#     백트래킹을 이용한 조합 생성 함수
    
#     Args:
#         start: 다음에 선택할 수 있는 가장 작은 수 (중복 방지용)
#         path: 현재까지 선택한 수들의 리스트
#     """
    
#     # ===== 기저 조건 (Base Case) =====
#     # M개를 모두 선택했다면 결과 출력하고 종료
#     if len(path) == M:
#         print(*path)  # 리스트의 원소들을 공백으로 구분하여 출력
#         return
    
#     # ===== 재귀 호출 부분 =====
#     # start부터 N까지의 수 중에서 하나씩 선택
#     for i in range(start, N + 1):
#         # 핵심 아이디어들:
#         # 1. i+1을 다음 start로 전달 → 오름차순 보장 & 중복 방지
#         # 2. path + [i]로 새 리스트 생성 → 자동 백트래킹 효과
        
#         print(f"  " * len(path) + f"선택: {i}, 현재 경로: {path + [i]}")  # 디버깅용
        
#         backtrack(i + 1, path + [i])
        
#         print(f"  " * len(path) + f"복귀: {i} 선택 해제")  # 디버깅용

# # 초기 호출: 1부터 시작, 빈 경로로 시작
# print(f"=== N={N}, M={M} 조합 생성 시작 ===")
# backtrack(1, [])