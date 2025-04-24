def insertion_sort_with_log(A):
    n = len(A)
    for i in range(1, n):
        current = A[i]
        j = i - 1
        
        # 적절한 위치 찾을 때까지 요소들을 오른쪽으로 이동
        while j >= 0 and A[j] > current:
            A[j + 1] = A[j]
            j -= 1
        
        # 현재 요소 삽입
        A[j + 1] = current
        print(f"[단계 {i}] {current}을(를) {j+1}번 위치에 삽입 → {A}")
    return A

# 예시 배열
arr = [15, 31, 65, 73, 8, 66, 11, 3, 20, 48, 29, 1, 33, 25, 4]
insertion_sort_with_log(arr)
print("\n최종 정렬 결과:", arr)
