
## 큐 Queue

# FIFO, 사람들 대기열과 같다.

# - 삽입/삭제 : O(1)

from collections import deque

dq = deque()
dq.append(123)
dq.appendleft(456)
dq.appendleft(789)

print(dq.pop())
print(dq.popleft())
