## 우선순위 큐

# - **삽입/삭제 : O(log N)**
#   - heappush, heappop 모두 O(log N) 시간 복잡도

# 우선순위 큐는 다음과 같은 상황에서 주로 사용됩니다:

# - **가장 우선순위가 높은(또는 낮은) 데이터를 빠르게 꺼내야 할 때**
# - **최단 경로 알고리즘** (예: 다익스트라 알고리즘)
# - **시뮬레이션에서 이벤트를 우선순위대로 처리할 때**
# - **작업 스케줄링** (우선순위가 높은 작업부터 처리)
# - **데이터 스트림에서 상위 N개 요소 유지**

# 즉, 데이터 중에서 "가장 중요한 것"을 반복적으로 빠르게 꺼내야 하는 문제에서 많이 사용됩니다.

import heapq
pq = []
heapq.heappush(pq,456)
heapq.heappush(pq,123)
heapq.heappush(pq,789)
print("size of pq:",len(pq))
# size of pq: 3 
print("pq:",pq)
# pq: [123, 456, 789]
# pq는 항상 정렬된 상태를 유지한다.
while len(pq) > 0:
    print(heapq.heappop(pq))
# 123
# 456
# 789