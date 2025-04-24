def selection_sort_with_log(A):
    n = len(A)
    for last in range(n-1, 0, -1):
        max_idx = 0
        for i in range(1, last+1):
            if A[i] > A[max_idx]:
                max_idx = i
        A[max_idx], A[last] = A[last], A[max_idx]
        print(f"After swapping index {max_idx} and {last}: {A}")

# 예시 배열
arr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
selection_sort_with_log(arr)
print("최종 정렬 결과:", arr)
