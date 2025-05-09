def partition(A, p, r):
    """
    A[p...r]를 pivot(A[r]) 기준으로 분할하고, pivot의 최종 위치(q)를 반환한다.
    """
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickselect(A, p, r, i):
    """
    A[p...r]에서 i번째로 작은 원소를 반환한다.
    평균 시간 복잡도: Θ(n), 최악 시간 복잡도: Θ(n^2)
    """
    if p == r:
        return A[p]
    q = partition(A, p, r)
    k = q - p + 1

    if i < k:
        return quickselect(A, p, q - 1, i)
    elif i == k:
        return A[q]
    else:
        return quickselect(A, q + 1, r, i - k)

if __name__ == "__main__":
    A = [7, 10, 4, 3, 20, 15]
    # 배열에서 3번째로 작은 원소를 찾으면 7이 출력된다
    print(quickselect(A.copy(), 0, len(A) - 1, 3))  # 출력: 7
