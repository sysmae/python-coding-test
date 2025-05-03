## 맵 Map(Dictionary)

# Key : Value 쌍으로 이루어진 데이터 구조
# 키 끼리는 중복이 불가능하다.
# 키를 통해서 값을 찾는 구조

# 파이썬은 해시로 구현된 딕셔너리 자료형을 제공한다.
# 삽입, 삭제, 탐색이 O(1)로 가능하다.
# 해시 충돌이 발생할 경우, O(N)으로 탐색해야 한다.

m = {}
m["Yoondy"] = 40
m["Sky"] = 30
m["Jerry"] = 50

print("Size of m:", len(m))
# Size of m: 3

print("m:", m)
# m: {'Yoondy': 40, 'Sky': 30, 'Jerry': 50}

for k in m:
    print(k, m[k])
# Yoondy 40
# Sky 30
# Jerry 50