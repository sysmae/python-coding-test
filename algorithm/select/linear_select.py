def linear_select(A, p, r, i):
    # [설명] A[p:r+1]에서 i번째로 작은 원소를 찾는 함수입니다.
    print(f"[linear_select] 호출: A[{p}:{r+1}]={A[p:r+1]}, i={i}")
    # [설명] 부분 배열의 크기가 5 이하이면 직접 정렬하여 i번째 원소를 반환합니다.
    if r - p + 1 <= 5:
        subarray = A[p:r+1]
        subarray.sort()
        print(f"[linear_select] 5 이하 부분 배열 정렬: {subarray}, 반환값: {subarray[i-1]}")
        return subarray[i-1]
    
    # [설명] 5개씩 그룹을 나누고 각 그룹의 중앙값을 구합니다.
    medians = []
    n = r - p + 1
    num_groups = (n + 4) // 5
    for g in range(num_groups):
        group_start = p + g * 5
        group_end = min(group_start + 4, r)
        group = A[group_start:group_end+1]
        group.sort()
        median_idx = (len(group) - 1) // 2
        medians.append(group[median_idx])
        print(f"[linear_select] 그룹 {g}: {group}, 중앙값: {group[median_idx]}")

    print(f"[linear_select] 중앙값 리스트: {medians}")
    # [설명] 중앙값들의 중앙값(Median of Medians, MoM)을 재귀적으로 구합니다.
    mom = linear_select(medians, 0, len(medians)-1, (len(medians)+1)//2)
    print(f"[linear_select] 중앙값들의 중앙값(MoM): {mom}")
    # [설명] MoM을 피벗으로 사용하기 위해 배열의 끝(r)으로 이동시킵니다.
    mom_idx = p
    while mom_idx <= r and A[mom_idx] != mom:
        mom_idx += 1
    A[mom_idx], A[r] = A[r], A[mom_idx]
    print(f"[linear_select] MoM을 맨 뒤로 이동: {A[p:r+1]}")
    
    # [설명] MoM을 피벗으로 파티션을 수행합니다.
    q = partition(A, p, r)
    print(f"[linear_select] partition 결과: q={q}, A={A[p:r+1]}")
    k = q - p + 1  # [설명] 피벗이 정렬된 배열에서 몇 번째인지 계산
    if i == k:
        print(f"[linear_select] k==i, 반환값: {A[q]}")
        return A[q]
    elif i < k:
        print(f"[linear_select] i<k, 왼쪽 재귀 호출")
        return linear_select(A, p, q - 1, i)
    else:
        print(f"[linear_select] i>k, 오른쪽 재귀 호출")
        return linear_select(A, q + 1, r, i - k)
    
def partition(A, p, r):
    # [설명] A[p:r+1]에서 A[r]을 피벗으로 하여 파티션을 수행합니다.
    pivot = A[r]
    print(f"[partition] 피벗: {pivot}, A[{p}:{r+1}]={A[p:r+1]}")
    i = p - 1
    for j in range(p, r):
        # [설명] 피벗 이하의 값은 왼쪽으로 이동
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    # [설명] 피벗을 올바른 위치로 이동
    A[i+1], A[r] = A[r], A[i+1]
    print(f"[partition] 파티션 완료: {A[p:r+1]}, 반환값: {i+1}")
    return i + 1

# 사용 예시
if __name__ == "__main__":
    # [설명] 3번째로 작은 원소(즉, 정렬 시 3번째 값)를 찾는 예시입니다.
    A = [17, 23, 5, 9, 12, 31, 8, 4, 15, 29, 2, 19, 11, 6, 27, 21, 13, 1, 25, 7, 10, 3, 20, 16, 14, 18, 22, 24, 26, 28, 30, 32, 33, 34, 35, 36, 37]
    print(linear_select(A.copy(), 0, len(A)-1, 3))  # 출력: 5
