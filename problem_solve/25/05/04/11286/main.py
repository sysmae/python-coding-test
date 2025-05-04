# https://www.acmicpc.net/problem/11286
# 문제
# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력
# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

# 출력
# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# 예제 입력 1 
# 18
# 1
# -1
# 0
# 0
# 0
# 1
# 1
# -1
# -1
# 2
# -2
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 예제 출력 1 
# -1
# 1
# 0
# -1
# -1
# 1
# 1
# -2
# 2
# 0

# # 방법1 절댓값 힙을 구현하기 위해 heapq를 사용한다.
# # heapq는 최소 힙을 구현하기 때문에, 절댓값을 기준으로 정렬하기 위해 튜플을 사용한다.
# # 튜플의 첫 번째 요소는 절댓값, 두 번째 요소는 원래 값이다.
# # 튜플의 첫 번째 요소를 기준으로 정렬하고, 두 번째 요소를 기준으로 정렬한다.

# arr = [(3,4),(3,1),(8,5),(3,2),(8,7)]
# arr.sort()
# print(arr)  # [(3, 1), (3, 2), (3, 4), (8, 5), (8, 7)]
# # 튜플의 첫 번째 요소를 기준으로 정렬하고, 두 번째 요소를 기준으로 정렬한다.
# # 위 방식을 사용하여 절댓값 힙을 구현한다.

# import heapq as hq
# import sys
# input = sys.stdin.readline
# n = int(input())
# pq = []

# for _ in range(n):
#     x = int(input())
#     if x:
#         hq.heappush(pq,(abs(x),x))
#     else:
#         if pq:
#             print(hq.heappop(pq)[1])
#         else:
#             print(0)


# # 방법2
# 양수는 min_heap에, 음수는 max_heap에 넣는다.
# 절댓값이 같은 경우에는 음수는 max_heap에서 꺼내고, 양수는 min_heap에서 꺼낸다.
import heapq as hq
import sys
input = sys.stdin.readline

min_heap = []
max_heap = [] 
for _ in range(int(input())):
  x = int(input())
  if x > 0 :
    hq.heappush(min_heap, x)
  elif x < 0:
    hq.heappush(max_heap, -x)
  else:
    if min_heap:
      if max_heap:
        if abs(min_heap[0]) < abs(max_heap[0]):
          print(hq.heappop(min_heap))
        elif abs(min_heap[0]) >= abs(max_heap[0]):
          print(-hq.heappop(max_heap))
      else:
        print(hq.heappop(min_heap))
    else:
      if max_heap:
        print(-hq.heappop(max_heap))
      else:
        print(0)
    