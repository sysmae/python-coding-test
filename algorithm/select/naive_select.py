def naive_select(A, p, r, i):
    """
    A[p...r]에서 i번째로 작은 원소를 반환한다.
    시간 복잡도: Θ(n^2)
    """
    # 구간이 하나의 원소만 남으면 그 원소가 답
    if p == r:
        return A[p]

    # A[p...r]에서 가장 작은 원소의 인덱스 k 찾기
    k = p
    for j in range(p + 1, r + 1):
        if A[j] < A[k]:
            k = j

    # i가 1이면 찾은 최소 원소를 바로 반환
    if i == 1:
        return A[k]

    # i > 1이면 A[k]를 배열에서 제거하기 위해 왼쪽으로 한 칸씩 당김
    for j in range(k, r):
        A[j] = A[j + 1]

    # r 범위를 하나 줄이고, i도 하나 줄여 재귀 호출
    return naive_select(A, p, r - 1, i - 1)


# 예시 사용
if __name__ == "__main__":
    A = [7, 10, 4, 3, 20, 15]
    # 3번째로 작은 원소를 찾으면 7이 출력됨
    print(naive_select(A.copy(), 0, len(A) - 1, 3))