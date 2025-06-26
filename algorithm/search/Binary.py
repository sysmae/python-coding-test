# 이진 탐색 Binary Search
# 이진 탐색은 정렬된 배열에서 특정 값을 찾는 알고리즘으로, 배열을 반으로 나누어 검색 범위를 줄여나가는 방식입니다.
# 이진 탐색은 O(log n)의 시간 복잡도를 가지며, 정렬된 배열에서만 사용할 수 있습니다.
# 정렬 (nlog n) + 이진 탐색 (log n) = O(n log n)
# 경우에 따라 선형 탐색보다 느릴 수 있다.
# 미리 정렬된 배열이 있다면 이진 탐색을 사용하여 O(log n)으로 검색할 수 있습니다.

# 라이브러리
from bisect import bisect_left, bisect_right

v = (0,1,3,3,6,6,6,7,8,8,9)
three = bisect_right(v,3) - bisect_left(v,3)
print(three) # 2
four = bisect_right(v,4) - bisect_left(v,4)
print(four) # 0
six = bisect_right(v,6) - bisect_left(v,6)
print(six) # 3

# 파라메트릭 서치
# 최적화 문제를 결정 문제로 바꾸어 이진탐색으로 푸는 방법

# 최적화 문제: 문제 상황을 만족하는 변수의 최댓값이나 최솟값을 찾는 문제
# 결정 문제: 주어진 조건을 만족하는지 여부를 판단하는 문제(YES/NO)

# 매개 변수가 주어지면 true 혹은 false가 결정 되어야 한다.
# 가능한 해의 영역이 연속적이어야 한다.
# 범위를 반씩 줄여가며 가운데 값이 true인지 false인지 판단한다.

def search(st, en, target):
  if st == en:
    return st
  mid = (st + en) // 2
  if target(mid):
    return search(mid + 1, en, target)
  else:
    return search(st, mid, target)