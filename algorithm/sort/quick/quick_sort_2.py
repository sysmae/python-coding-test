def quickSort(A, p, r, depth=0):
    indent = "  " * depth
    print(f"{indent}[quickSort] 깊이 {depth}: 범위 {p}~{r}, 현재 배열: {A[p:r+1]}")
    
    if p < r:
        q = partition(A, p, r, depth)
        print(f"{indent}[quickSort] 피벗 위치 확정: 인덱스 {q}, 현재 배열: {A[p:r+1]}")
        
        # 왼쪽 부분 정렬
        print(f"{indent}왼쪽 부분 정렬 시작 ({p}~{q-1})")
        quickSort(A, p, q-1, depth+1)
        
        # 오른쪽 부분 정렬
        print(f"{indent}오른쪽 부분 정렬 시작 ({q+1}~{r})")
        quickSort(A, q+1, r, depth+1)

def partition(A, p, r, depth=0):
    indent = "  " * depth
    pivot = A[p]
    print(f"{indent}[partition] 피벗 선택: {pivot}, 부분 배열: {A[p:r+1]}")
    
    i = p  # 피벗보다 작은 요소들의 마지막 인덱스
    for j in range(p+1, r+1):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            print(f"{indent}[partition] {A[j]}↔{A[i]} 교체 → {A[p:r+1]}")
    
    # 피벗 최종 위치 교환
    A[p], A[i] = A[i], A[p]
    print(f"{indent}[partition] 최종 피벗 위치 {i}: {A[p:r+1]}")
    return i

# 실행 예제
if __name__ == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print("정렬 전 배열:", array)
    quickSort(array, 0, len(array)-1)
    print("최종 정렬 결과:", array)
