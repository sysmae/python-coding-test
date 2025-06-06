# https://www.acmicpc.net/problem/11003
# 문제
# N개의 수 A1, A2, ..., AN과 L이 주어진다.

# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

# 입력
# 첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)

# 둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)

# 출력
# 첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.

# 예제 입력 1 
# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6
# 예제 출력 1 
# 1 1 1 2 2 2 2 2 3 3 2 2

# import sys
# from collections import deque

# input = sys.stdin.readline

# N,L= map(int,input().split())
# # 첫번째는 값, 두번째는 번째
# dq = deque()
# now = list(map(int,input().split()))

# for i in range(N):
#   # 나보다 큰 데이터 삭제
#   while dq and dq[-1][0] > now[i]:
#     dq.pop()
#   dq.append((now[i],i))

#   # 슬라이딩 윈도우 사이즈 L  벗어난 데이터 삭제. 인덱스 확인
#   if dq[0][1] <= i - L: # 윈도우 범위를 벗어나면
#     dq.popleft()
#   print(dq[0][0],end=' ')


import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
# deque에는 (값, 인덱스) 튜플을 저장
# 맨 앞에는 항상 현재 윈도우의 최솟값이 위치
dq = deque()
now = list(map(int, input().split()))

for i in range(N):
    # ===== 1단계: 뒤에서부터 불필요한 값들 제거 =====
    # 현재 값(now[i])보다 큰 값들은 절대 최솟값이 될 수 없으므로 제거
    # 왜냐하면 현재 값이 더 작고, 더 늦게 들어왔기 때문 (더 오래 유지됨)
    while dq and dq[-1][0] > now[i]:
        dq.pop()
    
    # ===== 2단계: 현재 값을 deque에 추가 =====
    # (값, 인덱스) 형태로 저장
    dq.append((now[i], i))
    
    # ===== 3단계: 윈도우 범위를 벗어난 값 제거 =====
    # 현재 윈도우: [i-L+1, i] 범위
    # dq[0][1] <= i - L 이면 윈도우 범위를 벗어남
    if dq[0][1] <= i - L:  # 윈도우 범위를 벗어나면
        dq.popleft()
    
    # ===== 4단계: 현재 윈도우의 최솟값 출력 =====
    # deque의 맨 앞 값이 항상 현재 윈도우의 최솟값
    print(dq[0][0], end=' ')
