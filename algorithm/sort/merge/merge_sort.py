def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = A[p:q+1]  # 왼쪽 부분 배열
    R = A[q+1:r+1]  # 오른쪽 부분 배열

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort_with_log(A, p, r, depth=0):
    if p < r:
        q = (p + r) // 2
        merge_sort_with_log(A, p, q, depth+1)
        merge_sort_with_log(A, q+1, r, depth+1)
        merge(A, p, q, r)
        print(f"{'  '*depth}After merging A[{p}:{r+1}]: {A[p:r+1]}")

# 예시 배열
arr = [31, 3, 65, 73, 8, 11, 20, 29, 48, 15]
merge_sort_with_log(arr, 0, len(arr)-1)
print("최종 정렬 결과:", arr)
