def bubble_sort_with_log(A):
    n = len(A)
    for last in range(n-1, 0, -1):
        for i in range(0, last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                print(f"Swapped index {i} and {i+1}: {A}")

# 예시 배열
arr = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
bubble_sort_with_log(arr)
print("최종 정렬 결과:", arr)
