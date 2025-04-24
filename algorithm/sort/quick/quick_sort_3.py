def quick_sort(A, p, r, depth=0):
    """
    퀵 정렬 메인 함수
    A: 정렬할 배열
    p: 시작 인덱스
    r: 끝 인덱스
    depth: 재귀 깊이 (로그 출력용)
    """
    indent = "  " * depth
    if p < r:
        print(f"{indent}[정렬 시작] 범위 {p}~{r}: {A[p:r+1]}")
        q = partition(A, p, r, depth)
        print(f"{indent}[피벗 고정] 인덱스 {q} → 값 {A[q]}")
        
        # 왼쪽 부분 배열 정렬
        print(f"{indent}↙ 왼쪽 하위 배열 정렬 ({p}~{q-1})")
        quick_sort(A, p, q-1, depth+1)
        
        # 오른쪽 부분 배열 정렬
        print(f"{indent}↘ 오른쪽 하위 배열 정렬 ({q+1}~{r})")
        quick_sort(A, q+1, r, depth+1)

def partition(A, p, r, depth=0):
    """
    분할 함수 (로무토 방식)
    A: 배열
    p: 시작 인덱스
    r: 끝 인덱스
    depth: 재귀 깊이
    """
    indent = "  " * depth
    x = A[r]  # 피벗 (마지막 원소)
    i = p - 1
    
    print(f"\n{indent}➊ 피벗 선택: {x} (인덱스 {r})")
    print(f"{indent}초기 상태: {A[p:r+1]}")

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
            print(f"{indent}→ swap [{i}]↔[{j}]: {A[p:r+1]}")
    
    # 피벗 최종 위치 교환
    A[i+1], A[r] = A[r], A[i+1]
    print(f"{indent}⇢ 최종 피벗 교환 [{i+1}]↔[{r}]: {A[p:r+1]}")
    return i + 1

# 실행 예제
if __name__ == "__main__":
    # sample_array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    sample_array = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]

    print("■ 최초 입력 배열:", sample_array)
    quick_sort(sample_array, 0, len(sample_array)-1)
    print("\n■ 최종 정렬 결과:", sample_array)
