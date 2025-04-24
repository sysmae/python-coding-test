

def quick_sort(arr, start, end, depth=0):
    """
    퀵 정렬 함수
    arr: 정렬할 배열
    start: 시작 인덱스
    end: 끝 인덱스
    depth: 재귀 깊이 (로그 출력용)
    """
    # 현재 배열 상태 출력
    indent = "  " * depth
    print(f"{indent}[퀵 정렬 호출] 깊이: {depth}, 배열: {arr[start:end+1]}")
    
    # 종료 조건: 정렬할 원소가 1개 이하인 경우
    if start >= end:
        return
    
    # 피벗 설정 (첫 번째 원소)
    pivot = arr[start]
    print(f"{indent}피벗 선택: {pivot}")
    
    # 분할 과정
    left = start + 1
    right = end
    
    print(f"{indent}분할 시작 - left: {left}, right: {right}")
    
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= pivot:
            left += 1
        
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= pivot:
            right -= 1
        
        # 엇갈렸다면 피벗과 작은 데이터를 교체
        if left > right:
            arr[start], arr[right] = arr[right], arr[start]
            print(f"{indent}피벗과 작은 데이터 교체: {arr[start:end+1]}")
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
            print(f"{indent}큰 데이터와 작은 데이터 교체: {arr[start:end+1]}")
    
    print(f"{indent}분할 완료 - 피벗 위치: {right}, 분할된 배열: {arr[start:end+1]}")
    
    # 재귀적으로 왼쪽 부분과 오른쪽 부분 정렬
    print(f"{indent}왼쪽 부분 배열 정렬 시작: {arr[start:right]}")
    quick_sort(arr, start, right - 1, depth + 1)
    
    print(f"{indent}오른쪽 부분 배열 정렬 시작: {arr[right+1:end+1]}")
    quick_sort(arr, right + 1, end, depth + 1)

# 실행 예제
if __name__ == "__main__":
    # 테스트할 배열
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    
    print("정렬 전 배열:", array)
    quick_sort(array, 0, len(array) - 1)
    print("정렬 후 배열:", array)
